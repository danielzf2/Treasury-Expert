/* Treasury Expert — Simulador TPF + Derivativos */

const ALL_INSTRUMENTS = ["LTN","NTN-F","NTN-B","LFT","DI1","DAP","DOL","DDI","FRC"];
const CORR_TYPES = ["Nenhuma","% na taxa","R$/contrato","R$/titulo"];
const SCENARIOS = {
    bull_par:"Bull Parallel", bear_par:"Bear Parallel",
    bull_steep:"Bull Steepener", bear_steep:"Bear Steepener",
    bull_flat:"Bull Flattener", bear_flat:"Bear Flattener",
    pos_fly:"Positive Butterfly", neg_fly:"Negative Butterfly",
    custom:"Custom"
};
const SCENARIO_DESCS = {
    bull_par:"Todas as taxas caem de forma paralela. Bom para posições compradas em duration.",
    bear_par:"Todas as taxas sobem de forma paralela. Bom para posições vendidas em duration.",
    bull_steep:"Curtos caem mais que longos. Mostra exposição a inclinação quando o vértice curto lidera o rally.",
    bear_steep:"Longos sobem mais que curtos. Captura abertura de prêmio de prazo.",
    bull_flat:"Longos caem mais que curtos. Útil para testar fechamento da parte longa.",
    bear_flat:"Curtos sobem mais que longos. Útil em choque de política monetária no front-end da curva.",
    pos_fly:"Barriga sobe e pontas caem. Testa risco de curvatura contra posições concentradas no miolo.",
    neg_fly:"Barriga cai e pontas sobem. Testa ganho/perda em estruturas compradas na barriga.",
    custom:"Combina paralelo, inclinação e curvatura com os sliders abaixo.",
};

function brDate() {
    const now = new Date();
    const utcMs = now.getTime();
    const brMs = utcMs - 3 * 60 * 60 * 1000;
    const br = new Date(brMs);
    return br.getUTCFullYear() + "-" +
        String(br.getUTCMonth() + 1).padStart(2, "0") + "-" +
        String(br.getUTCDate()).padStart(2, "0");
}

function fmtMoney(v, digits=0) {
    return `R$ ${(v || 0).toLocaleString("pt-BR",{maximumFractionDigits:digits, minimumFractionDigits:digits})}`;
}

function fmtNumber(v, digits=2) {
    return (v || 0).toLocaleString("pt-BR",{maximumFractionDigits:digits, minimumFractionDigits:digits});
}

const state = {
    legs: [],
    presets: {},
    marketData: null,
    vnaData: null,
    anbimaTpfData: null,
    sourcesStatus: null,
    results: null,
    scenarioKey: "bull_par",
    magnitude: 10,
    customParallel: 0, customSlope: 0, customCurvature: 0,
    deltaFx: 0, deltaIpca: 0, deltaCupom: 0,
    expandFlows: false,
    activeTab: "sim",
    activeChartTab: "curve",
    activeSimSubTab: "pernas",
};

async function init() {
    document.getElementById("dataNeg").value = brDate();
    const resp = await fetch("/sim/presets");
    state.presets = await resp.json();
    renderPresets();
    await fetchMarketData();
    applyPreset(Object.keys(state.presets)[0]);
}

function renderPresets() {
    const el = document.getElementById("presets");
    el.innerHTML = Object.keys(state.presets).map(name =>
        `<button onclick="applyPreset('${name}')">${name}</button>`
    ).join("");
}

function applyPreset(name) {
    state.legs = state.presets[name].map(l => ({...l}));
    renderLegs();
    processLegs();
}

function switchTab(tab) {
    state.activeTab = tab;
    document.querySelectorAll(".tabs button").forEach((b,i) => {
        b.classList.toggle("active", ["sim","mkt","formulas"][i] === tab);
    });
    document.getElementById("tab-sim").style.display = tab === "sim" ? "" : "none";
    document.getElementById("tab-mkt").style.display = tab === "mkt" ? "" : "none";
    document.getElementById("tab-formulas").style.display = tab === "formulas" ? "" : "none";

    if (tab === "sim" && state.activeSimSubTab === "cenarios") {
        requestAnimationFrame(() => resizeScenarioCharts());
    }
}

function switchSimSubTab(name) {
    state.activeSimSubTab = name;
    document.querySelectorAll("#simSubTabs button").forEach((b, i) => {
        b.classList.toggle("active", ["pernas","cenarios","detalhes"][i] === name);
    });
    document.getElementById("subtab-pernas").style.display   = name === "pernas"   ? "" : "none";
    document.getElementById("subtab-cenarios").style.display = name === "cenarios" ? "" : "none";
    document.getElementById("subtab-detalhes").style.display = name === "detalhes" ? "" : "none";

    if (name === "cenarios") {
        requestAnimationFrame(() => resizeScenarioCharts());
    }
}

function resizeScenarioCharts() {
    ["chartContainer","pnlBarsChart","pnlConsolidatedChart","pnlPerLegChart"].forEach(id => {
        const el = document.getElementById(id);
        if (el && el._fullLayout) Plotly.Plots.resize(id);
    });
}

const _tickerCache = {};

async function fetchTickers(instrument) {
    if (_tickerCache[instrument]) return _tickerCache[instrument];
    try {
        const resp = await fetch(`/sim/tickers/${instrument}`);
        const data = await resp.json();
        _tickerCache[instrument] = data.tickers || [];
        return _tickerCache[instrument];
    } catch(e) { return []; }
}

const HEDGE_MODES = [
    {v: "manual", l: "Manual"},
    {v: "maturity", l: "Vencimento"},
    {v: "duration", l: "Duration"},
    {v: "strip", l: "Strip (perfeito)"},
];

function renderLegs() {
    const hdr = document.getElementById("legsHeader");
    const headerCols = [
        {label: "Instrumento", cls: ""},
        {label: "Ticker",      cls: ""},
        {label: "C/V",         cls: "col-ctr"},
        {label: "Qtd",         cls: "col-num"},
        {label: "Taxa (%)",    cls: "col-num"},
        {label: "VNA",         cls: "col-num"},
        {label: "Hedge",       cls: ""},
        {label: "Corretagem",  cls: ""},
        {label: "Valor",       cls: "col-num"},
        {label: "",            cls: "col-ctr"},
    ];
    hdr.innerHTML = headerCols.map(c => `<div class="${c.cls}">${c.label}</div>`).join("");

    const c = document.getElementById("legsContainer");
    c.innerHTML = state.legs.map((leg, i) => {
        const isNTNB = leg.instrument === "NTN-B";
        const isCoupon = leg.instrument === "NTN-F" || leg.instrument === "NTN-B";
        const vnaVal = leg.vna || "";
        const hedgeMode = leg.hedge_mode || "manual";
        const isAuto = !!leg.auto;
        const rowCls = isAuto ? "leg-row leg-row-auto" : "leg-row";
        return `<div class="${rowCls}">
            <div>
                ${isAuto ? '<span class="auto-badge">AUTO</span>' : ''}
                <select onchange="changeInstrument(${i},this.value)">${ALL_INSTRUMENTS.map(inst =>
                    `<option ${inst===leg.instrument?"selected":""}>${inst}</option>`).join("")}</select>
            </div>
            <div><select id="ticker_${i}" onchange="updateLeg(${i},'ticker',this.value)">
                <option value="${leg.ticker}">${leg.ticker}</option></select></div>
            <div><select onchange="updateLeg(${i},'direction',this.value)">
                <option value="C" ${leg.direction==="C"?"selected":""}>Compra</option>
                <option value="V" ${leg.direction==="V"?"selected":""}>Venda</option></select></div>
            <div><input type="number" value="${leg.quantity}" onchange="updateLeg(${i},'quantity',+this.value)"></div>
            <div><input type="number" value="${leg.taxa}" step="0.005" onchange="updateLeg(${i},'taxa',+this.value)"></div>
            <div>${isNTNB ? `<input type="number" value="${vnaVal}" step="0.01" placeholder="VNA" onchange="updateLeg(${i},'vna',+this.value||null)">` : `<span class="muted" style="font-size:10px">—</span>`}</div>
            <div>${isCoupon && !isAuto ? `<select onchange="changeHedgeMode(${i},this.value)">${HEDGE_MODES.map(h =>
                `<option value="${h.v}" ${h.v===hedgeMode?"selected":""}>${h.l}</option>`).join("")}</select>` : `<span class="muted" style="font-size:10px">—</span>`}</div>
            <div><select onchange="updateLeg(${i},'corr_type',this.value)">${CORR_TYPES.map(ct =>
                `<option ${ct===leg.corr_type?"selected":""}>${ct}</option>`).join("")}</select></div>
            <div><input type="number" value="${leg.corr_value}" step="0.001" onchange="updateLeg(${i},'corr_value',+this.value)"></div>
            <div>${state.legs.length > 1 ? `<button class="btn-remove" onclick="removeLeg(${i})">✕</button>` : ""}</div>
        </div>`;
    }).join("");

    state.legs.forEach((leg, i) => populateTickerSelect(i, leg.instrument, leg.ticker));
}

function changeHedgeMode(i, mode) {
    state.legs[i].hedge_mode = mode;
    state.legs = state.legs.filter(l => !l.auto);
    renderLegs();
    processLegs();
}

const _MONTH_NAMES = ["", "Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"];
const _TPF_INSTRUMENTS = new Set(["LTN", "NTN-F", "NTN-B", "LFT"]);
const _TICKER_TO_MONTH_LOCAL = {F:1,G:2,H:3,J:4,K:5,M:6,N:7,Q:8,U:9,V:10,X:11,Z:12};

function tickerLabel(ticker, instrument) {
    /* Para TPF mostra 'Set/26' (mes/ano), para derivativos mantem 'F32'. */
    if (!_TPF_INSTRUMENTS.has(instrument)) return ticker;
    const m = ticker.toUpperCase().match(/^([FGHJKMNQUVXZ])(\d{2})$/);
    if (!m) return ticker;
    const month = _TICKER_TO_MONTH_LOCAL[m[1]];
    return `${_MONTH_NAMES[month]}/${m[2]}`;
}

async function populateTickerSelect(i, instrument, currentTicker) {
    const sel = document.getElementById(`ticker_${i}`);
    if (!sel) return;
    const tickers = await fetchTickers(instrument);
    if (!tickers.length) {
        sel.innerHTML = `<option value="${currentTicker}">${tickerLabel(currentTicker, instrument)}</option>`;
        return;
    }
    const found = tickers.includes(currentTicker);
    sel.innerHTML = tickers.map(t =>
        `<option value="${t}" ${t === currentTicker ? "selected" : ""}>${tickerLabel(t, instrument)}</option>`
    ).join("");
    if (!found && currentTicker) {
        sel.insertAdjacentHTML("afterbegin",
            `<option value="${currentTicker}" selected>${tickerLabel(currentTicker, instrument)}</option>`);
    }
}

async function changeInstrument(i, inst) {
    state.legs[i].instrument = inst;
    if (inst === "NTN-B") {
        const vnaFromFeed = state.vnaData?.vna_ntnb;
        if (!state.legs[i].vna || state.legs[i].vna === 4500.0) {
            state.legs[i].vna = vnaFromFeed && vnaFromFeed > 0 ? vnaFromFeed : 4500.0;
        }
    }
    const tickers = await fetchTickers(inst);
    if (tickers.length) state.legs[i].ticker = tickers[0];
    _autoFillRate(state.legs[i]);
    renderLegs();
    processLegs();
}

function updateLeg(i, field, val) {
    const leg = state.legs[i];
    leg[field] = val;
    if (leg.auto && ["quantity","taxa","ticker","direction"].includes(field)) {
        leg.auto = false;
        for (let j = i - 1; j >= 0; j--) {
            const inst = state.legs[j].instrument;
            if ((inst === "NTN-F" || inst === "NTN-B") && !state.legs[j].auto) {
                state.legs[j].hedge_mode = "manual";
                break;
            }
        }
    }
    if (field === "ticker") _autoFillRate(leg);
    processLegs();
}

function _autoFillRate(leg) {
    /* Puxa taxa de mercado quando trocamos instrumento/ticker.
       Para TPF: usa ANBIMA tx_indicativa; para derivativos: B3 last/ajuste. */
    if (!state.marketData) return;
    const r = findMarketRate(leg.instrument, leg.ticker, state.marketData);
    if (r !== null && r > 0) leg.taxa = r;
}

function addLeg() {
    state.legs.push({instrument:"LTN",ticker:"F32",direction:"C",quantity:2000,taxa:13.76,corr_type:"Nenhuma",corr_value:0.0});
    renderLegs();
    processLegs();
}

function removeLeg(i) {
    state.legs.splice(i, 1);
    renderLegs();
    processLegs();
}

async function fetchMarketData() {
    const btn = document.getElementById("btnFetchMarket");
    btn.disabled = true; btn.textContent = "Carregando...";

    const sources = {b3_bcb: null, vna: null, anbima_tpf: null};
    const t0 = Date.now();

    try {
        const [mktRes, vnaRes, tpfRes] = await Promise.allSettled([
            fetch("/sim/market-data").then(r => r.json()),
            fetch("/sim/vna").then(r => r.json()),
            fetch("/sim/anbima-tpf").then(r => r.json()),
        ]);

        if (mktRes.status === "fulfilled") {
            state.marketData = mktRes.value;
            sources.b3_bcb = {ok: true, data: state.marketData};
        } else {
            sources.b3_bcb = {ok: false, error: String(mktRes.reason)};
        }

        if (vnaRes.status === "fulfilled") {
            state.vnaData = vnaRes.value;
            const ok = (state.vnaData.records || []).length > 0;
            sources.vna = {ok, data: state.vnaData};
        } else {
            sources.vna = {ok: false, error: String(vnaRes.reason)};
        }

        if (tpfRes.status === "fulfilled") {
            state.anbimaTpfData = tpfRes.value;
            const ok = (state.anbimaTpfData.records || []).length > 0;
            sources.anbima_tpf = {ok, data: state.anbimaTpfData};
        } else {
            sources.anbima_tpf = {ok: false, error: String(tpfRes.reason)};
        }

        state.sourcesStatus = {
            ts: new Date().toLocaleTimeString("pt-BR"),
            elapsed_ms: Date.now() - t0,
            sources,
        };

        if (state.marketData) {
            document.getElementById("mktTimestamp").textContent = `Atualizado: ${state.marketData.timestamp}`;
        }
        Object.keys(_tickerCache).forEach(k => delete _tickerCache[k]);
        if (state.marketData) renderMarketIndicators();
        renderMarketDataTab();
        if (state.marketData) {
            updateLegsFromMarket();
            processLegs();
        }
    } catch(e) { console.error(e); }
    btn.disabled = false; btn.textContent = "Atualizar Dados de Mercado";
}

function renderMarketIndicators() {
    const m = state.marketData; if (!m) return;
    const el = document.getElementById("mktIndicators");
    el.style.display = "";
    el.innerHTML = [
        {l:"CDI", v:`${m.cdi_aa.toFixed(2)}%`},
        {l:"PTAX", v:m.ptax.toFixed(4)},
        {l:"Spot USD", v:m.spot_usd > 0 ? `~${m.spot_usd.toFixed(2)}` : "--"},
        {l:"Atualizado", v:m.timestamp},
    ].map(({l,v}) => `<div class="metric"><div class="label">${l}</div><div class="value">${v}</div></div>`).join("");
    if (m.spot_usd > 0) document.getElementById("spotInput").value = m.spot_usd.toFixed(4);
}

function updateLegsFromMarket() {
    if (!state.marketData) return;
    const m = state.marketData;
    state.legs.forEach(leg => {
        const rate = findMarketRate(leg.instrument, leg.ticker, m);
        if (rate !== null) leg.taxa = rate;
    });
    renderLegs();
}

function findMarketRate(inst, ticker, m) {
    ticker = ticker.toUpperCase().trim();

    // Derivativos: vem do feed B3 (cotacao.b3.com.br)
    const sources = {DI1: m.di1, DOL: m.dol, FRC: m.frc, DAP: m.dap, DDI: m.ddi};
    if (sources[inst]) {
        const c = sources[inst].find(c => c.symb === inst + ticker);
        if (c) return c.last > 0 ? c.last : c.ajuste;
    }

    // TPF: vem do feed ANBIMA (PU oficial + tx indicativa D-1)
    const tpfFeed = state.anbimaTpfData?.records || [];
    if (["LTN", "NTN-F", "NTN-B", "LFT"].includes(inst) && tpfFeed.length) {
        const targetVcto = inst === "NTN-B" ? tickerToDateNTNB(ticker) : tickerToDateStr(ticker);
        if (targetVcto) {
            const r = tpfFeed.find(x => x.instrument === inst && x.data_vencimento === targetVcto);
            if (r && r.tx_indicativa) return r.tx_indicativa;
        }
    }

    return null;
}

function tickerToDateStr(ticker) {
    // 'F32' -> '2032-01-01' (LTN/NTN-F/LFT)
    const m = ticker.toUpperCase().match(/^([FGHJKMNQUVXZ])(\d{2})$/);
    if (!m) return null;
    const month = _TICKER_TO_MONTH_LOCAL[m[1]];
    const yr = 2000 + parseInt(m[2]);
    return `${yr}-${String(month).padStart(2,"0")}-01`;
}

function tickerToDateNTNB(ticker) {
    // 'K29' -> '2029-05-15' (NTN-B sempre dia 15)
    const m = ticker.toUpperCase().match(/^([FGHJKMNQUVXZ])(\d{2})$/);
    if (!m) return null;
    const month = _TICKER_TO_MONTH_LOCAL[m[1]];
    const yr = 2000 + parseInt(m[2]);
    return `${yr}-${String(month).padStart(2,"0")}-15`;
}

async function processLegs() {
    const body = {
        legs: state.legs.filter(l => !l.auto),
        data_neg: document.getElementById("dataNeg").value,
        spot: +document.getElementById("spotInput").value,
        di1: state.marketData?.di1 || [],
        dap: state.marketData?.dap || [],
    };
    try {
        const resp = await fetch("/sim/process", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
        state.results = await resp.json();
        if (state.results && state.results.legs) {
            state.legs = state.results.legs.map(l => ({
                instrument: l.instrument,
                ticker: l.ticker,
                direction: l.direction,
                quantity: l.quantity,
                taxa: l.taxa,
                corr_type: l.corr_type || "Nenhuma",
                corr_value: l.corr_value || 0.0,
                vna: l.vna || null,
                hedge_mode: l.hedge_mode || "manual",
                auto: l.auto || false,
                auto_for: l.auto_for,
            }));
            renderLegs();
        }
        renderResults();
        renderScenarios();
    } catch(e) { console.error(e); }
}

function renderResults() {
    const r = state.results; if (!r) return;
    renderMetrics(r);
    renderAvTable(r);
    renderRiskFactors(r);
    renderDetails(r);
    renderSpreadCosts(r);
    renderCashflows(r);
    renderHedge(r);
}

function renderMetrics(r) {
    const el = document.getElementById("metricsArea");
    const s = r.strategy;
    let items = [];
    if (s.type === "casada") {
        const allin = (s.spread - r.total_corr_bps).toFixed(2);
        items = [{l:"Spread All-in",v:`${allin} bps`},{l:"Retorno Equivalente",v:`${s.bmk} ${allin>=0?"+":""}${allin} bps`},
            {l:"Nocional",v:`R$ ${(r.legs.find(l=>l.info_type==="tpf")?.noc/1e6||0).toFixed(1)}M`},{l:"Corretagem Total",v:`R$ ${r.total_corr.toFixed(0)}`}];
    } else if (s.type === "cupom_sint") {
        items = [{l:"Cupom Cambial Implícito",v:`${s.cupom.toFixed(2)}% a.a.`},{l:"DOL Futuro",v:s.dol_taxa.toFixed(1)},
            {l:"Spot",v:document.getElementById("spotInput").value},{l:"DI1",v:`${s.di_taxa.toFixed(3)}%`}];
    } else if (s.type === "dol_sint" || s.type === "dol_sint_ddi") {
        items = [{l:"Dólar Forward Sintético",v:`~${(s.fwd||0).toFixed(2)}`},{l:"DI1",v:`${s.di_taxa.toFixed(3)}%`},
            {l:s.frc_inst||"FRC",v:`${(s.frc_taxa||0).toFixed(3)}%`},{l:"Spot",v:document.getElementById("spotInput").value}];
    } else if (s.type === "single" && r.legs.length === 1) {
        const l = r.legs[0];
        items = [{l:"Taxa",v:l.info_conv==="price"?l.taxa.toFixed(1):`${l.taxa.toFixed(3)}%`},{l:"PU",v:l.pu.toFixed(2)},
            {l:"Financeiro",v:l.info_conv!=="price"?`R$ ${l.fin.toLocaleString("pt-BR",{maximumFractionDigits:0})}`:"--"},{l:"DV01 Total",v:`R$ ${l.dv01_total.toFixed(0)}`}];
    } else {
        items = [{l:"Estratégia",v:s.result.substring(0,40)},{l:"Financeiro Total",v:`R$ ${r.total_fin.toLocaleString("pt-BR",{maximumFractionDigits:0})}`},
            {l:"DV01 Total",v:`R$ ${r.total_dv01.toFixed(0)}`},{l:"Corretagem Total",v:`R$ ${r.total_corr.toFixed(0)}`}];
    }
    el.innerHTML = `<div class="metrics">${items.map(({l,v})=>`<div class="metric"><div class="label">${l}</div><div class="value">${v}</div></div>`).join("")}</div>`;
}

function renderAvTable(r) {
    const el = document.getElementById("avTable");
    const autoLegs = r.legs.filter(l => l.auto);
    const userLegs = r.legs.filter(l => !l.auto);
    const aggregateAuto = autoLegs.length >= 3;

    let html = '<div class="av-wrap"><table class="sim-tbl"><tr><th></th><th>Instrumento</th><th class="tc">Ativo</th><th class="tc">Passivo</th><th class="tc">Vcto</th></tr>';
    userLegs.forEach(l => {
        const isBuy = l.direction === "C";
        const dirLabel = isBuy ? "Compra" : "Venda";
        const dirColor = isBuy ? "#3fb950" : "#f85149";
        html += `<tr><td><span style="color:${dirColor};font-weight:600">${dirLabel}</span></td>
            <td class="bold">${l.instrument}</td><td class="tc mono">${l.exp_ativo}</td>
            <td class="tc mono">${l.exp_passivo}</td><td class="tc mono muted">${l.parsed_label}</td></tr>`;
    });
    if (aggregateAuto) {
        const isBuy = autoLegs[0].direction === "C";
        const dirLabel = isBuy ? "Compra" : "Venda";
        const dirColor = isBuy ? "#3fb950" : "#f85149";
        const hedgeInst = autoLegs[0].instrument;
        const minVcto = autoLegs[0].parsed_label;
        const maxVcto = autoLegs[autoLegs.length-1].parsed_label;
        html += `<tr style="opacity:0.75"><td><span class="auto-badge">AUTO</span> <span style="color:${dirColor};font-weight:600">${dirLabel}</span></td>
            <td class="bold">${hedgeInst} Hedge × ${autoLegs.length}</td>
            <td class="tc mono muted" colspan="2">strip de ${minVcto} a ${maxVcto}</td>
            <td class="tc mono muted">${autoLegs.length} vértices</td></tr>`;
    } else {
        autoLegs.forEach(l => {
            const isBuy = l.direction === "C";
            const dirLabel = isBuy ? "Compra" : "Venda";
            const dirColor = isBuy ? "#3fb950" : "#f85149";
            html += `<tr style="opacity:0.7"><td><span class="auto-badge">AUTO</span> <span style="color:${dirColor};font-weight:600">${dirLabel}</span></td>
                <td class="bold">${l.instrument}</td><td class="tc mono">${l.exp_ativo}</td>
                <td class="tc mono">${l.exp_passivo}</td><td class="tc mono muted">${l.parsed_label}</td></tr>`;
        });
    }
    html += `<tr class="av-result"><td colspan="5">${r.strategy.result}</td></tr></table></div>`;
    el.innerHTML = html;
}

function renderRiskFactors(r) {
    const el = document.getElementById("riskFactors");
    if (!r.risk_factors || !r.risk_factors.length) { el.innerHTML = ""; return; }
    let html = '<div class="sim-card"><div class="sim-card-h">Fatores de Risco</div><table class="sim-tbl"><tr><th>Fator</th><th class="tc">Status</th><th>Descrição</th></tr>';
    r.risk_factors.forEach(f => {
        const cls = f.exposto ? "pill-exp" : "pill-hdg";
        const txt = f.exposto ? "EXPOSTO" : "HEDGEADO";
        html += `<tr><td class="bold">${f.fator}</td><td class="tc"><span class="${cls}">${txt}</span></td><td class="muted" style="font-size:10px">${f.desc}</td></tr>`;
    });
    html += "</table></div>";
    el.innerHTML = html;
}

function renderDetails(r) {
    const el = document.getElementById("detailsTable");
    const cols = [
        {label: "Instr.",    cls: ""},
        {label: "Dir.",      cls: ""},
        {label: "Lado",      cls: ""},
        {label: "Vcto",      cls: ""},
        {label: "Liq",       cls: ""},
        {label: "DU",        cls: "tc"},
        {label: "DC",        cls: "tc"},
        {label: "Taxa",      cls: "tr"},
        {label: "Final",     cls: "tr"},
        {label: "PU",        cls: "tr"},
        {label: "Financeiro",cls: "tr"},
        {label: "D.Mac",     cls: "tr"},
        {label: "D.Mod",     cls: "tr"},
        {label: "DV01/un",   cls: "tr"},
        {label: "DV01 Tot",  cls: "tr"},
        {label: "Corr R$",   cls: "tr"},
        {label: "Corr bps",  cls: "tr"},
    ];
    let html = '<table class="sim-tbl"><tr>' + cols.map(c=>`<th class="${c.cls}">${c.label}</th>`).join("") + "</tr>";
    r.legs.forEach(l => {
        const isP = l.info_conv === "price";
        const rowCls = l.auto ? ' style="opacity:0.65"' : '';
        const autoMark = l.auto ? '<span class="auto-badge" style="margin-right:4px">A</span>' : '';
        html += `<tr${rowCls}>
            <td>${autoMark}${l.instrument}</td><td>${l.direction==="C"?"Compra":"Venda"}</td><td>${l.side}</td>
            <td>${l.parsed_full}</td><td class="mono">${l.liq}</td>
            <td class="tc mono">${l.du}</td><td class="tc mono">${l.dc}</td>
            <td class="tr mono">${isP?l.taxa.toFixed(1):l.taxa.toFixed(4)+"%"}</td>
            <td class="tr mono">${isP?l.tax_fin.toFixed(1):l.tax_fin.toFixed(4)+"%"}</td>
            <td class="tr mono">${isP?l.pu.toFixed(1):l.pu.toFixed(2)}</td>
            <td class="tr mono">${isP?"--":"R$ "+l.fin.toLocaleString("pt-BR",{maximumFractionDigits:0})}</td>
            <td class="tr mono">${l.d_mac.toFixed(2)}</td><td class="tr mono">${l.d_mod.toFixed(2)}</td>
            <td class="tr mono">${l.dv01_unit.toFixed(2)}</td><td class="tr mono">${l.dv01_total.toFixed(0)}</td>
            <td class="tr mono">${l.corr_brl.toFixed(2)}</td><td class="tr mono">${l.corr_bps.toFixed(2)}</td></tr>`;
    });
    html += "</table>";
    el.innerHTML = html;
}

function renderSpreadCosts(r) {
    const el = document.getElementById("spreadCosts");
    if (r.strategy.type !== "casada") { el.innerHTML = ""; return; }
    const allin = r.strategy.spread - r.total_corr_bps;
    const visibleLegs = r.legs.filter(l => l.info_conv !== "price" && (l.corr_brl > 0 || !l.auto));
    let html = '<hr class="divider"><div class="two-col"><div><div class="sec-h">Spread All-in</div><table class="sim-tbl"><tr><th>Item</th><th class="tr">Valor</th></tr>';
    html += `<tr><td>Spread bruto</td><td class="tr">${r.strategy.spread.toFixed(2)} bps</td></tr>`;
    visibleLegs.forEach(l => {
        if (l.corr_bps > 0.001) {
            html += `<tr><td>Corretagem ${l.instrument}${l.auto?" (auto)":""}</td><td class="tr">-${l.corr_bps.toFixed(2)} bps</td></tr>`;
        }
    });
    html += `<tr><td class="bold">Spread all-in</td><td class="tr bold">${allin.toFixed(2)} bps</td></tr></table></div>`;
    html += '<div><div class="sec-h">Custos</div><table class="sim-tbl"><tr><th>Item</th><th class="tr">R$</th><th class="tr">bps</th></tr>';
    visibleLegs.forEach(l => {
        if (l.corr_brl > 0.01) {
            html += `<tr><td>Corretagem ${l.instrument}${l.auto?" (auto)":""} (${l.parsed_label})</td><td class="tr">${l.corr_brl.toFixed(2)}</td><td class="tr">-${l.corr_bps.toFixed(2)}</td></tr>`;
        }
    });
    html += `<tr><td class="bold">Total</td><td class="tr bold">R$ ${r.total_corr.toFixed(2)}</td><td class="tr bold">-${r.total_corr_bps.toFixed(2)}</td></tr></table></div></div>`;
    el.innerHTML = html;
}

function renderCashflows(r, flowPnl=[]) {
    const el = document.getElementById("krdSection");
    const legs = (r.legs || []).filter(l => l.cashflows && l.cashflows.flows && l.cashflows.flows.length);
    if (!legs.length) { el.innerHTML = ""; return; }

    const pnlByLeg = new Map(flowPnl.map(fp => [`${fp.instrument}:${fp.ticker}:${fp.direction}`, fp]));
    let html = '<hr class="divider">';
    legs.forEach((l, idx) => {
        const cf = l.cashflows;
        const pnl = pnlByLeg.get(`${l.instrument}:${l.ticker}:${l.direction}`);
        const pnlMetricClass = pnl ? (pnl.total >= 0 ? "green" : "red") : "";
        html += `<div class="sim-card"><div class="sim-card-h">Fluxos, Cupons e Principal — ${l.instrument} ${l.parsed_label}</div>`;
        html += '<div class="metrics">';
        html += `<div class="metric"><div class="label">PV dos Fluxos</div><div class="value">${fmtMoney(cf.pv_total,2)}</div></div>`;
        html += `<div class="metric"><div class="label">Duration Macaulay</div><div class="value">${fmtNumber(cf.duration_macaulay,2)} anos</div></div>`;
        html += `<div class="metric"><div class="label">Duration ANBIMA</div><div class="value">${fmtNumber(cf.duration_anbima_du,0)} DU</div></div>`;
        html += `<div class="metric"><div class="label">P&L por Fluxo</div><div class="value ${pnlMetricClass}">${pnl?fmtMoney(pnl.total,0):"--"}</div></div>`;
        html += '</div>';
        html += `<div id="krdChart${idx}" style="min-height:260px"></div>`;
        html += '<div style="overflow-x:auto"><table class="sim-tbl"><tr><th>Fluxo</th><th>Data</th><th class="tc">DU</th><th class="tr">Nominal</th><th class="tr">PV</th><th class="tr">Peso</th><th class="tr">KRD</th><th class="tr">Delta</th><th class="tr">P&L</th></tr>';
        cf.flows.forEach(f => {
            const pf = pnl?.flows?.find(x => x.label === f.label && x.du === f.du);
            const pnlClass = pf ? (pf.pnl > 1 ? " green" : (pf.pnl < -1 ? " red" : "")) : "";
            html += `<tr><td>${f.label}</td><td class="mono">${f.payment_date || "--"}</td><td class="tc mono">${f.du}</td>`;
            html += `<td class="tr mono">${fmtMoney(f.nominal,2)}</td><td class="tr mono">${fmtMoney(f.pv,2)}</td>`;
            html += `<td class="tr mono">${fmtNumber(f.peso*100,1)}%</td><td class="tr mono">${fmtNumber(f.krd,4)}</td>`;
            html += `<td class="tr mono">${pf?fmtNumber(pf.delta_bps,1)+" bps":"--"}</td><td class="tr mono${pnlClass}">${pf?fmtMoney(pf.pnl,0):"--"}</td></tr>`;
        });
        html += `<tr class="av-result"><td>Total</td><td></td><td></td><td></td><td class="tr mono">${fmtMoney(cf.pv_total,2)}</td><td class="tr mono">100,0%</td><td class="tr mono">${fmtNumber(cf.duration_macaulay,4)}</td><td></td><td class="tr mono">${pnl?fmtMoney(pnl.total,0):"--"}</td></tr>`;
        html += '</table></div></div>';
    });
    el.innerHTML = html;

    legs.forEach((l, idx) => {
        const flows = l.cashflows.flows;
        Plotly.newPlot(`krdChart${idx}`, [{
            x: flows.map(f => `${f.label}<br>${f.payment_date || f.du+" DU"}`),
            y: flows.map(f => f.krd),
            type: "bar",
            marker: {color: "#58a6ff"},
            text: flows.map(f => fmtNumber(f.krd,3)),
            textposition: "outside",
        }], {
            template:"none",
            paper_bgcolor:"rgba(0,0,0,0)",
            plot_bgcolor:"rgba(0,0,0,0)",
            font:{family:"Inter, -apple-system, BlinkMacSystemFont, sans-serif", size:11, color:"#c9d1d9"},
            margin:{l:50,r:20,t:20,b:70},
            height:280,
            xaxis:{gridcolor:"rgba(100,100,100,0.15)"},
            yaxis:{title:"Contribuição para duration (anos)", gridcolor:"rgba(100,100,100,0.15)"},
            showlegend:false,
        }, {displayModeBar:false, responsive:true});
    });
}

function renderHedge(r) {
    const el = document.getElementById("hedgeSection");
    if (!el) return;
    const h = r.hedge;
    if (!h || !h.tpf) { el.innerHTML = ""; return; }

    const inst = h.hedge_instrument || "DI1";
    const tpfInst = h.tpf.instrument || "NTN-F";

    let html = '<hr class="divider"><div class="sim-card">';
    html += `<div class="sim-card-h">Hedge de ${tpfInst} com ${inst} — 3 Modalidades</div>`;

    html += '<div class="metrics" style="margin-bottom:12px">';
    html += `<div class="metric"><div class="label">DV01 Total ${tpfInst}</div><div class="value">R$ ${fmtNumber(h.tpf.dv01_total,0)}</div></div>`;
    html += `<div class="metric"><div class="label">${inst} atual</div><div class="value">${h.current_n} contratos</div></div>`;
    html += `<div class="metric"><div class="label">DV01 residual</div><div class="value">R$ ${fmtNumber(h.dv01_residual,0)}</div></div>`;
    html += '</div>';

    html += '<div style="overflow-x:auto"><table class="sim-tbl">';
    html += `<tr><th>Modalidade</th><th class="tc">Vértice ${inst}</th><th class="tr">DV01/contrato</th><th class="tr">Contratos</th><th>Obs</th></tr>`;

    html += `<tr><td class="bold">1. No Vencimento</td><td class="tc mono">${h.du_maturity} DU</td>`;
    html += `<td class="tr mono">R$ ${fmtNumber(h.dv01_at_maturity,2)}</td>`;
    html += `<td class="tr mono">${h.n_at_maturity}</td>`;
    html += `<td class="muted" style="font-size:10px">Aproximação — descasa duration para títulos com cupom</td></tr>`;

    html += `<tr><td class="bold">2. Na Duration</td><td class="tc mono">${h.du_duration} DU</td>`;
    html += `<td class="tr mono">R$ ${fmtNumber(h.dv01_at_duration,2)}</td>`;
    html += `<td class="tr mono">${h.n_at_duration}</td>`;
    html += `<td class="muted" style="font-size:10px">Casamento de DV01 no prazo médio — funciona bem para shifts paralelos</td></tr>`;

    html += `<tr class="av-result"><td class="bold">3. Strip (Hedge Perfeito)</td><td class="tc">ver abaixo</td>`;
    html += `<td></td><td class="tr mono bold">${h.n_strip_total || 0}</td>`;
    html += `<td class="muted" style="font-size:10px">1 ${inst} por fluxo — elimina risco de inclinação e curvatura</td></tr>`;
    html += '</table></div>';

    if (h.strip && h.strip.length) {
        html += `<div style="margin-top:12px"><p style="font-size:12px;color:#8b949e;margin-bottom:4px">Detalhamento do Strip — ${inst} por fluxo de ${tpfInst}</p>`;
        html += '<div style="overflow-x:auto"><table class="sim-tbl">';
        html += `<tr><th>Fluxo</th><th>Data</th><th class="tc">DU</th><th class="tr">PV Fluxo</th><th class="tr">DV01 Fluxo</th><th class="tr">DV01/${inst}</th><th class="tr">Contratos ${inst}</th></tr>`;
        let totalDv01 = 0, totalN = 0;
        h.strip.forEach(s => {
            totalDv01 += s.dv01_flow || 0;
            totalN += s.hedge_n || 0;
            html += `<tr><td>${s.label}</td><td class="mono">${s.payment_date || "--"}</td><td class="tc mono">${s.du}</td>`;
            html += `<td class="tr mono">${fmtMoney(s.pv_flow_total,0)}</td>`;
            html += `<td class="tr mono">${fmtNumber(s.dv01_flow,2)}</td>`;
            html += `<td class="tr mono">${fmtNumber(s.hedge_dv01_unit,2)}</td>`;
            html += `<td class="tr mono">${s.hedge_n}</td></tr>`;
        });
        html += `<tr class="av-result"><td class="bold">Total</td><td></td><td></td><td></td>`;
        html += `<td class="tr mono bold">${fmtNumber(totalDv01,2)}</td><td></td>`;
        html += `<td class="tr mono bold">${totalN}</td></tr>`;
        html += '</table></div></div>';
    }

    html += '</div>';
    el.innerHTML = html;
}

function renderScenarios() {
    if (!state.results) return;
    const hasRateLegs = state.results.legs.some(l => l.info_conv !== "price");
    const hasDol = state.results.legs.some(l => l.instrument === "DOL");
    if (!hasRateLegs && !hasDol) return;

    renderScenarioRadio();
    renderSliders();
    loadCharts();
}

function renderScenarioRadio() {
    const el = document.getElementById("scenarioRadio");
    el.innerHTML = Object.entries(SCENARIOS).map(([k,v]) =>
        `<label><input type="radio" name="scenario" value="${k}" ${k===state.scenarioKey?"checked":""} onchange="changeScenario('${k}')"><span>${v}</span></label>`
    ).join("");
    document.getElementById("scenarioDesc").textContent = SCENARIO_DESCS[state.scenarioKey] || "";
}

function changeScenario(key) {
    state.scenarioKey = key;
    renderScenarioRadio();
    renderSliders();
    loadCharts();
}

function renderSliders() {
    const r = state.results; if (!r) return;
    const hasIpca = r.legs.some(l => ["NTN-B","DAP"].includes(l.instrument));
    const hasCupom = r.legs.some(l => ["FRC","DDI"].includes(l.instrument)) || (r.legs.some(l=>l.instrument==="DOL") && r.legs.some(l=>l.instrument==="DI1"));
    const hasFx = r.legs.some(l => l.instrument === "DOL");

    const preInsts = r.legs.filter(l => ["LTN","NTN-F","DI1"].includes(l.instrument)).map(l => l.instrument);
    const preLabel = preInsts.length ? preInsts.filter((v,i,a)=>a.indexOf(v)===i).join(", ") : "DI1, LTN, NTN-F";

    const el = document.getElementById("slidersPanel");
    let html = '<div class="slider-header">Choques de Cenário</div>';
    html += '<p class="slider-hint">Mova os sliders para chocar taxas e ver o impacto no P&L. Positivo = direção do cenário, negativo = direção oposta.</p>';
    if (state.scenarioKey === "custom") {
        html += sliderHtml("Paralelo", "customParallel", state.customParallel, -50, 50, 1, "Shift uniforme em todos os vértices");
        html += sliderHtml("Inclinação", "customSlope", state.customSlope, -50, 50, 1, "Diferença curto vs longo");
        html += sliderHtml("Curvatura", "customCurvature", state.customCurvature, -50, 50, 1, "Barriga vs pontas");
    } else {
        html += sliderHtml("Cenário (bps)", "magnitude", state.magnitude, -50, 50, 1, `Aplica o cenário selecionado a ${preLabel}`);
    }
    if (hasFx) html += sliderHtml("Câmbio (%)", "deltaFx", state.deltaFx, -10, 10, 0.5, "Variação % no spot USD/BRL — afeta DOL");
    if (hasIpca) html += sliderHtml("Taxa Real (bps)", "deltaIpca", state.deltaIpca, -50, 50, 1, "Choque na taxa real IPCA — afeta NTN-B, DAP");
    if (hasCupom) html += sliderHtml("Cup. Cambial (bps)", "deltaCupom", state.deltaCupom, -50, 50, 1, "Choque no cupom cambial — afeta FRC, DDI");
    el.innerHTML = html;
}

function sliderHtml(label, key, val, min, max, step, hint) {
    return `<div class="slider-group">
        <label>${label} <span class="slider-val" id="val_${key}">${val}</span></label>
        <input type="range" min="${min}" max="${max}" step="${step}" value="${val}"
            oninput="state.${key}=+this.value;document.getElementById('val_${key}').textContent=this.value;loadCharts()">
        ${hint ? `<div class="slider-hint">${hint}</div>` : ""}
    </div>`;
}

async function loadCharts() {
    if (!state.results) return;
    const r = state.results;
    const di1 = state.marketData?.di1 || [];
    const dap = state.marketData?.dap || [];
    const base = {legs: r.legs, scenario_key: state.scenarioKey, magnitude: state.magnitude,
        delta_fx_pct: state.deltaFx, delta_ipca_bps: state.deltaIpca, delta_cupom_bps: state.deltaCupom,
        custom_parallel_bps: state.customParallel, custom_slope_bps: state.customSlope,
        custom_curvature_bps: state.customCurvature,
        di1: di1, dap: dap};

    const plotCfg = {displayModeBar:false, responsive:true};

    async function safeChart(url, body, divId) {
        try {
            const resp = await fetch(url, {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
            if (!resp.ok) { console.error(url, resp.status, await resp.text()); return null; }
            const fig = await resp.json();
            if (fig.data && divId) {
                await Plotly.newPlot(divId, fig.data, fig.layout, plotCfg);
                requestAnimationFrame(() => Plotly.Plots.resize(divId));
            }
            return fig;
        } catch(e) { console.error(url, e); return null; }
    }

    const [curve, pnl, cons, perLeg, mtm] = await Promise.all([
        safeChart("/sim/charts/curve", base, "chartContainer"),
        safeChart("/sim/charts/pnl-bars", base, "pnlBarsChart"),
        safeChart("/sim/charts/pnl-consolidated", base, "pnlConsolidatedChart"),
        safeChart("/sim/charts/pnl-per-leg", {...base, expand_flows: !!state.expandFlows}, "pnlPerLegChart"),
        safeChart("/sim/mtm-table", base, null),
    ]);

    if (mtm && mtm.total_pnl !== undefined) {
        document.getElementById("pnlTotal").innerHTML =
            `<div class="pnl-hero">
                <div class="pnl-hero-label">P&L Total do Cenário</div>
                <div class="pnl-hero-value ${mtm.total_pnl>=0?"green":"red"}">R$ ${mtm.total_pnl>=0?"+":""}${mtm.total_pnl.toLocaleString("pt-BR",{maximumFractionDigits:0})}</div>
            </div>`;
    }
    if (mtm && mtm.table) renderMtmTable(mtm.table, r.legs);
    if (mtm && mtm.flow_pnl) renderCashflows(r, mtm.flow_pnl);

    renderPnlPerLegToggle();
    renderChartTabs();
}

function renderPnlPerLegToggle() {
    const r = state.results;
    if (!r) return;
    const hasCoupon = r.legs.some(l => ["NTN-F","NTN-B"].includes(l.instrument) && !l.auto);
    const el = document.getElementById("pnlPerLegToggle");
    if (!el) return;
    if (!hasCoupon) { el.innerHTML = ""; return; }
    el.innerHTML = `<label style="display:flex;align-items:center;gap:6px;font-size:12px;color:#8b949e;cursor:pointer">
        <input type="checkbox" ${state.expandFlows?"checked":""} onchange="state.expandFlows=this.checked;loadCharts()" style="cursor:pointer">
        Detalhar P&L por fluxo (cupons + principal) na NTN-F/NTN-B
    </label>`;
}

function renderChartTabs() {
    if (!state.results) return;
    const r = state.results;
    const hasCupom = r.legs.some(l=>["FRC","DDI"].includes(l.instrument)) || (r.legs.some(l=>l.instrument==="DOL")&&r.legs.some(l=>l.instrument==="DI1"));
    const hasFwd = r.legs.some(l=>l.instrument==="DOL") || ["dol_sint","cupom_sint"].includes(r.strategy.type);
    const hasIpca = r.legs.some(l=>["NTN-B","DAP"].includes(l.instrument));

    const tabs = [{id:"curve", label:"Curva Pré"}];
    if (hasCupom) tabs.push({id:"cupom", label:"Cupom Cambial"});
    if (hasFwd) tabs.push({id:"forward", label:"Dólar Forward"});
    if (hasIpca) tabs.push({id:"real", label:"Taxa Real"});

    if (tabs.length <= 1) { document.getElementById("chartTabs").innerHTML = ""; return; }
    document.getElementById("chartTabs").innerHTML = tabs.map(t =>
        `<button class="${t.id===state.activeChartTab?"active":""}" onclick="switchChartTab('${t.id}')">${t.label}</button>`
    ).join("");
}

async function switchChartTab(tab) {
    state.activeChartTab = tab;
    renderChartTabs();
    const r = state.results;
    const base = {legs:r.legs, scenario_key:state.scenarioKey, magnitude:state.magnitude,
        delta_fx_pct:state.deltaFx, delta_ipca_bps:state.deltaIpca, delta_cupom_bps:state.deltaCupom,
        custom_parallel_bps:state.customParallel, custom_slope_bps:state.customSlope,
        custom_curvature_bps:state.customCurvature};
    let url, body;
    if (tab === "curve") { url="/sim/charts/curve"; body={...base, di1:state.marketData?.di1||[], dap:state.marketData?.dap||[]}; }
    else if (tab === "cupom") { url="/sim/charts/cupom"; body={frc_contracts:state.marketData?.frc||[], delta_cupom_bps:state.deltaCupom, legs:r.legs}; }
    else if (tab === "forward") { url="/sim/charts/forward"; body={di1:state.marketData?.di1||[], frc:state.marketData?.frc||[], spot:+document.getElementById("spotInput").value, ...base}; }
    else if (tab === "real") { url="/sim/charts/real"; body={dap_contracts:state.marketData?.dap||[], delta_ipca_bps:state.deltaIpca, legs:r.legs}; }
    const resp = await fetch(url, {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
    const fig = await resp.json();
    if (fig.data) Plotly.newPlot("chartContainer", fig.data, fig.layout, {displayModeBar:false, responsive:true});
}

function renderMtmTable(table, legs) {
    const el = document.getElementById("mtmTable");
    const autoIdxs = legs.map((l, i) => l.auto ? i : -1).filter(i => i >= 0);
    const userIdxs = legs.map((l, i) => l.auto ? -1 : i).filter(i => i >= 0);
    const aggregateAuto = autoIdxs.length >= 3;

    const cols = [];
    userIdxs.forEach(i => cols.push({label: `${legs[i].instrument} ${legs[i].parsed_label}`, idxs: [i], isAuto: false}));
    if (aggregateAuto) {
        const hedgeInst = legs[autoIdxs[0]].instrument;
        cols.push({label: `AUTO ${hedgeInst} Hedge (${autoIdxs.length})`, idxs: autoIdxs, isAuto: true});
    } else {
        autoIdxs.forEach(i => cols.push({label: `AUTO ${legs[i].instrument} ${legs[i].parsed_label}`, idxs: [i], isAuto: true}));
    }

    let html = '<div class="sim-card"><div class="sim-card-h">Tabela de Cenários MtM (per-leg P&L)</div><div style="overflow-x:auto"><table class="sim-tbl"><tr><th class="tc">Magnitude (bps)</th>';
    cols.forEach(c => html += `<th class="tr${c.isAuto?' muted':''}">${c.label}</th>`);
    html += '<th class="tr bold">Total</th></tr>';
    table.forEach(row => {
        const bg = row.delta === 0 ? ' style="background:#1c2128"' : '';
        html += `<tr${bg}><td class="tc mono">${row.delta}</td>`;
        cols.forEach(c => {
            const pnl = c.idxs.reduce((s, i) => s + (row.pnls[i] || 0), 0);
            const cc = pnl > 1 ? " green" : (pnl < -1 ? " red" : "");
            html += `<td class="tr mono${cc}">R$ ${pnl>=0?"+":""}${Math.round(pnl).toLocaleString("pt-BR")}</td>`;
        });
        const totCc = row.total > 1 ? " green" : (row.total < -1 ? " red" : "");
        html += `<td class="tr mono bold${totCc}">R$ ${row.total>=0?"+":""}${Math.round(row.total).toLocaleString("pt-BR")}</td></tr>`;
    });
    html += "</table></div></div>";
    el.innerHTML = html;
}

function renderMarketDataTab() {
    const m = state.marketData;
    const el = document.getElementById("mktDataContent");

    let html = renderSourcesStatus();

    if (!m) {
        el.innerHTML = html || `<p class="muted">Sem dados de mercado disponiveis.</p>`;
        return;
    }

    html += `<p class="muted" style="margin-bottom:12px">Atualizado: ${m.timestamp}</p>`;
    html += '<div class="metrics">';
    html += `<div class="metric"><div class="label">CDI Over</div><div class="value">${m.cdi_aa.toFixed(2)}% a.a.</div></div>`;
    html += `<div class="metric"><div class="label">CDI Dia</div><div class="value">${m.cdi_over_dia.toFixed(6)}%</div></div>`;
    html += `<div class="metric"><div class="label">PTAX Venda</div><div class="value">R$ ${m.ptax.toFixed(4)}</div></div>`;
    html += `<div class="metric"><div class="label">Spot USD</div><div class="value">${m.spot_usd>0?"R$ "+m.spot_usd.toFixed(4):"--"}</div></div></div>`;

    html += renderVnaTable();

    html += '<hr class="divider">';
    html += renderMktTable("Curva DI Futuro (B3)", m.di1, ["symb","vcto","last","bid","ask","ajuste"]);
    html += '<div class="two-col">';
    html += renderMktTable("DAP — Cupom IPCA (B3)", m.dap, ["symb","vcto","last","ajuste"]);
    html += renderMktTable("FRC — Cupom Cambial (B3)", m.frc.filter(c=>c.ajuste>0), ["symb","vcto","last","ajuste"]);
    html += '</div><div class="two-col">';
    html += renderMktTable("DOL — Dólar Futuro (B3)", m.dol, ["symb","vcto","last","bid","ask","ajuste"]);
    html += renderMktTable("DDI — Cupom Cambial Sujo (B3)", m.ddi.filter(c=>c.ajuste>0||c.last>0), ["symb","vcto","last","ajuste"]);
    html += '</div>';

    html += renderAnbimaTpfTables();

    el.innerHTML = html;
}

function renderSourcesStatus() {
    const s = state.sourcesStatus;
    if (!s) return '';

    const m = state.marketData;
    const vna = state.vnaData;
    const tpf = state.anbimaTpfData;
    const cards = [];

    // B3 derivativos
    if (s.sources.b3_bcb && s.sources.b3_bcb.ok && m) {
        const counts = [
            `DI1: ${(m.di1||[]).length}`,
            `DAP: ${(m.dap||[]).length}`,
            `FRC: ${(m.frc||[]).length}`,
            `DDI: ${(m.ddi||[]).length}`,
            `DOL: ${(m.dol||[]).length}`,
        ].join(" · ");
        cards.push({status:"ok", title:"B3 — Derivativos", subtitle:counts,
                    detail:`${m.timestamp} · cotacao.b3.com.br`});
    } else {
        cards.push({status:"err", title:"B3 — Derivativos", subtitle:"Falha ao buscar",
                    detail: s.sources.b3_bcb?.error || "sem resposta"});
    }

    // BCB indicadores
    if (m) {
        const cdi = m.cdi_aa>0 ? `CDI ${m.cdi_aa.toFixed(2)}%` : null;
        const ptax = m.ptax>0 ? `PTAX ${m.ptax.toFixed(4)}` : null;
        const parts = [cdi, ptax].filter(Boolean).join(" · ");
        cards.push({status: parts?"ok":"warn", title:"BCB — Indicadores",
                    subtitle: parts || "sem dados",
                    detail:"api.bcb.gov.br · CDI, PTAX, Selic, IPCA"});
    } else {
        cards.push({status:"err", title:"BCB — Indicadores", subtitle:"--", detail:"sem dados"});
    }

    // VNA Brasil Indicadores
    if (s.sources.vna && s.sources.vna.ok && vna) {
        const ntnb = vna.vna_ntnb;
        const lft = vna.vna_lft;
        const dataRef = vna.records[0]?.data_ref || "--";
        const parts = [];
        if (ntnb) parts.push(`NTN-B R$ ${ntnb.toFixed(6)}`);
        if (lft) parts.push(`LFT R$ ${lft.toFixed(6)}`);
        cards.push({status:"ok", title:"VNA — Brasil Indicadores",
                    subtitle: parts.join(" · "),
                    detail:`ref ${dataRef} · brasilindicadores.com.br`});
    } else {
        cards.push({status:"err", title:"VNA — Brasil Indicadores",
                    subtitle:"Indisponivel — usando fallback",
                    detail: s.sources.vna?.error || "feed offline"});
    }

    // ANBIMA TPF
    if (s.sources.anbima_tpf && s.sources.anbima_tpf.ok && tpf) {
        const records = tpf.records || [];
        const byInst = {};
        records.forEach(r => { byInst[r.instrument] = (byInst[r.instrument]||0) + 1; });
        const counts = Object.entries(byInst).map(([k,v]) => `${k}: ${v}`).join(" · ");
        cards.push({status:"ok", title:"ANBIMA — TPF (PU oficial)",
                    subtitle: counts || "sem registros",
                    detail:`ref ${tpf.data_ref || "--"} · anbima.com.br/ms{YYMMDD}.txt`});
    } else {
        cards.push({status:"err", title:"ANBIMA — TPF (PU oficial)",
                    subtitle:"Feed indisponivel",
                    detail: s.sources.anbima_tpf?.error || "feed D-1 nao publicado ainda"});
    }

    const cardsHtml = cards.map(c => {
        const dot = `<span class="src-dot src-${c.status}"></span>`;
        return `<div class="source-card">
            <div class="source-head">${dot}<span class="source-title">${c.title}</span></div>
            <div class="source-sub">${c.subtitle}</div>
            <div class="source-detail muted">${c.detail}</div>
        </div>`;
    }).join("");

    return `<div style="margin-bottom:8px">
        <h3 style="font-size:14px;margin-bottom:8px">Fontes de Dados <span class="muted" style="font-size:11px;font-weight:400">· consultadas em ${s.ts} (${s.elapsed_ms}ms)</span></h3>
        <div class="source-grid">${cardsHtml}</div>
    </div>
    <hr class="divider">`;
}

function renderVnaTable() {
    const vna = state.vnaData;
    if (!vna || !vna.records || !vna.records.length) return '';
    const rows = vna.records.map(r => `
        <tr>
            <td>${r.instrument}</td>
            <td class="mono tr">R$ ${r.vna.toLocaleString("pt-BR", {minimumFractionDigits:6, maximumFractionDigits:6})}</td>
            <td>${r.data_ref}</td>
            <td class="muted">${r.indice_str || ""}</td>
        </tr>`).join("");
    return `<div style="margin-top:16px">
        <h3 style="font-size:14px;margin-bottom:8px">VNA D0 (Brasil Indicadores)</h3>
        <table class="sim-tbl">
            <thead><tr><th>Titulo</th><th class="tr">VNA</th><th>Data Ref</th><th>Indice</th></tr></thead>
            <tbody>${rows}</tbody>
        </table>
    </div>`;
}

function renderAnbimaTpfTables() {
    const tpf = state.anbimaTpfData;
    if (!tpf || !tpf.records || !tpf.records.length) return '';

    const byInst = {};
    tpf.records.forEach(r => {
        if (!byInst[r.instrument]) byInst[r.instrument] = [];
        byInst[r.instrument].push(r);
    });

    const order = ["LTN", "NTN-F", "NTN-B", "LFT", "NTN-C"];
    let html = '<hr class="divider">';
    html += `<h3 style="font-size:14px;margin-bottom:8px">ANBIMA — Titulos Publicos (PU oficial · ref ${tpf.data_ref})</h3>`;
    html += '<div class="two-col">';
    let count = 0;
    for (const inst of order) {
        const rows = byInst[inst];
        if (!rows || !rows.length) continue;
        if (count > 0 && count % 2 === 0) html += '</div><div class="two-col">';
        const trs = rows.map(r => `
            <tr>
                <td>${r.data_vencimento}</td>
                <td class="mono tr">${r.tx_indicativa.toFixed(4)}%</td>
                <td class="mono tr">${r.pu.toLocaleString("pt-BR", {minimumFractionDigits:6, maximumFractionDigits:6})}</td>
                <td class="muted tr">${r.tx_compra.toFixed(4)} / ${r.tx_venda.toFixed(4)}</td>
            </tr>`).join("");
        html += `<div>
            <h4 style="font-size:13px;margin:8px 0">${inst} <span class="muted" style="font-weight:400">(${rows.length})</span></h4>
            <table class="sim-tbl">
                <thead><tr><th>Vencimento</th><th class="tr">Tx Indic</th><th class="tr">PU</th><th class="tr">Compra/Venda</th></tr></thead>
                <tbody>${trs}</tbody>
            </table>
        </div>`;
        count++;
    }
    html += '</div>';
    return html;
}

function renderMktTable(title, data, cols) {
    if (!data || !data.length) return `<div><h3 style="font-size:14px;margin-bottom:8px">${title}</h3><p class="muted">Sem dados</p></div>`;
    const numericCols = new Set(["last","bid","ask","ajuste"]);
    const colCls = c => numericCols.has(c) ? "tr" : (c === "vcto" ? "tc" : "");
    let html = `<div><h3 style="font-size:14px;margin-bottom:8px">${title}</h3><div style="overflow-x:auto;max-height:400px"><table class="sim-tbl"><tr>`;
    cols.forEach(c => html += `<th class="${colCls(c)}">${c}</th>`);
    html += "</tr>";
    data.forEach(row => {
        html += "<tr>";
        cols.forEach(c => {
            let v = row[c];
            if (typeof v === "number") v = v === 0 ? "—" : (Number.isInteger(v) ? v.toLocaleString("pt-BR") : v);
            const cls = `mono ${colCls(c)}`.trim();
            html += `<td class="${cls}">${v}</td>`;
        });
        html += "</tr>";
    });
    html += "</table></div></div>";
    return html;
}

function renderFormulas() {
    const K = (tex) => { try { return katex.renderToString(tex, {displayMode:true,throwOnError:false}); } catch(e) { return `<pre>${tex}</pre>`; } };
    const k = (tex) => { try { return katex.renderToString(tex, {displayMode:false,throwOnError:false}); } catch(e) { return `<code>${tex}</code>`; } };

    document.getElementById("formulasContent").innerHTML = `
    <p class="muted" style="margin-bottom:12px">Todas as fórmulas usadas no simulador. Convenções do mercado brasileiro.</p>

    <div class="sim-card"><div class="sim-card-h">Títulos Públicos (TPF)</div><div style="padding:16px">
    <h4>LTN — Zero-Coupon Prefixado</h4>
    ${K("PU = \\frac{1.000}{(1 + taxa)^{DU/252}}")}
    <p class="muted" style="font-size:11px">Exponencial, base 252 DU. Truncamento ANBIMA: T-6.</p>
    <h4 style="margin-top:16px">NTN-F — Prefixado com Cupom Semestral</h4>
    ${K("Cup_{sem} = (1{,}10)^{0{,}5} - 1 = 4{,}880885\\%")}
    ${K("PU = \\sum_{i=1}^{n} \\frac{Cup \\times VN}{(1 + TIR)^{DU_i/252}} + \\frac{VN}{(1 + TIR)^{DU_n/252}}")}
    <h4 style="margin-top:16px">NTN-B — IPCA+ com Cupom Semestral</h4>
    ${K("Cup_{sem} = (1{,}06)^{0{,}5} - 1 = 2{,}956301\\%")}
    ${K("PU = \\frac{Cotação}{100} \\times VNA")}
    <p class="muted" style="font-size:11px">Cotação truncada 4 casas (T-4). VNA truncado 6 casas (T-6).</p>
    <h4 style="margin-top:16px">LFT — Tesouro Selic</h4>
    ${K("PU = \\frac{Cotação}{100} \\times VNA_{Selic}")}
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Derivativos de Taxa de Juros</div><div style="padding:16px">
    <h4>DI1 — Futuro de DI</h4>
    ${K("PU = \\frac{100.000}{(1 + taxa)^{DU/252}}")}
    <p class="muted" style="font-size:11px">Face R$ 100.000. Vencimento: 1º DU do mês.</p>
    <h4 style="margin-top:16px">DAP — Futuro de Cupom de IPCA</h4>
    ${K("PU = \\frac{100.000}{(1 + cupom_{IPCA})^{DU/252}}")}
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Derivativos de Câmbio</div><div style="padding:16px">
    <h4>DOL — Dólar Futuro</h4>
    ${K("AJ = (PA - PO) \\times qtd \\times 50")}
    <p class="muted" style="font-size:11px">Cotação em R$ por USD 1.000. Multiplicador: R$ 50/ponto.</p>
    <h4 style="margin-top:16px">DDI — Cupom Cambial Sujo</h4>
    ${K("PU = \\frac{100.000}{1 + taxa \\times \\frac{DC}{360}}")}
    <h4 style="margin-top:16px">FRC — FRA de Cupom Cambial (Limpo)</h4>
    ${K("PU = \\frac{50.000}{1 + cupom \\times \\frac{DC}{360}}")}
    <h4 style="margin-top:16px">Cupom Cambial Implícito (DOL + DI1)</h4>
    ${K("cupom = \\left[\\frac{Spot \\times 1000}{DOL} \\times (1 + DI)^{DU/252} - 1\\right] \\times \\frac{360}{DC} \\times 100")}
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Duration e Risco</div><div style="padding:16px">
    <h4>Duration de Macaulay</h4>
    ${K("D_{mac} = \\frac{\\sum_{i=1}^{n} t_i \\times PV_i}{\\sum_{i=1}^{n} PV_i}")}
    <h4 style="margin-top:16px">Duration Modificada</h4>
    ${K("D_{mod} = \\frac{D_{mac}}{1 + taxa}")}
    <h4 style="margin-top:16px">DV01 (Dollar Value of 01)</h4>
    ${K("DV01 = D_{mod} \\times PU \\times 0{,}0001")}
    <h4 style="margin-top:16px">Aproximação de Preço (Taylor 2ª ordem)</h4>
    ${K("\\frac{\\Delta P}{P} \\approx -D_{mod} \\times \\Delta y + \\frac{1}{2} C \\times (\\Delta y)^2")}
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Interpolação Flat Forward (B3 V14)</div><div style="padding:16px">
    ${K("fwd = \\left[\\frac{(1+r_2)^{DU_2/252}}{(1+r_1)^{DU_1/252}}\\right]^{252/(DU_2-DU_1)} - 1")}
    ${K("r_{alvo} = \\left[(1+r_1)^{DU_1/252} \\times (1+fwd)^{(DU_{alvo}-DU_1)/252}\\right]^{252/DU_{alvo}} - 1")}
    <p class="muted" style="font-size:11px">Premissa: taxa forward constante entre vértices adjacentes. Manual de Curvas B3 V14.</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Conversões de Taxa</div><div style="padding:16px">
    <h4>CDI + Spread vs Pré</h4>
    ${K("(1 + CDI) \\times (1 + Spread) = (1 + Pré)")}
    <p class="muted" style="font-size:11px">NUNCA somar CDI + Spread diretamente. A composição é multiplicativa.</p>
    <h4 style="margin-top:16px">Fisher (Nominal vs Real)</h4>
    ${K("(1 + nominal) = (1 + real) \\times (1 + inflação)")}
    <h4 style="margin-top:16px">Linear 360 vs Exponencial 252</h4>
    ${K("exp_{252} = \\left(1 + lin_{360} \\times \\frac{DC}{360}\\right)^{252/DU} - 1")}
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Cenários de Curva</div><div style="padding:16px">
    <p class="muted" style="font-size:11px;margin-bottom:12px">${k("t")} = posição normalizada na curva (${k("-1")} = curto, ${k("+1")} = longo)</p>
    <h4>Paralelo (Shift)</h4>${K("\\Delta_i = \\pm magnitude")}
    <h4 style="margin-top:12px">Steepener / Flattener</h4>${K("\\Delta_i = magnitude \\times t_i")}
    <h4 style="margin-top:12px">Butterfly</h4>${K("\\Delta_i = magnitude \\times (1 - t_i^2) - \\frac{magnitude}{2}")}
    </div></div>`;
}

document.addEventListener("DOMContentLoaded", () => {
    init();
    if (typeof katex !== "undefined") { renderFormulas(); }
    else { document.querySelector('script[src*="katex"]').addEventListener("load", renderFormulas); }
});

let _resizeTimer;
window.addEventListener("resize", () => {
    clearTimeout(_resizeTimer);
    _resizeTimer = setTimeout(() => resizeScenarioCharts(), 200);
});

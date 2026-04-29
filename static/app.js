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

const state = {
    legs: [],
    presets: {},
    marketData: null,
    results: null,
    scenarioKey: "bull_par",
    magnitude: 10,
    deltaFx: 0, deltaIpca: 0, deltaCupom: 0,
    activeTab: "sim",
    activeChartTab: "curve",
};

async function init() {
    const resp = await fetch("/sim/presets");
    state.presets = await resp.json();
    renderPresets();
    applyPreset(Object.keys(state.presets)[0]);
    fetchMarketData();
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
}

function renderLegs() {
    const hdr = document.getElementById("legsHeader");
    hdr.innerHTML = ["Instrumento","Ticker","C/V","Qtd","Taxa (%)","Liquidação","Corretagem","Valor",""].map(
        h => `<div style="color:#8b949e;font-size:10px;text-transform:uppercase;letter-spacing:.3px">${h}</div>`
    ).join("");

    const c = document.getElementById("legsContainer");
    c.innerHTML = state.legs.map((leg, i) => {
        const isPrice = ["DOL"].includes(leg.instrument);
        return `<div class="leg-row">
            <div><select onchange="updateLeg(${i},'instrument',this.value)">${ALL_INSTRUMENTS.map(inst =>
                `<option ${inst===leg.instrument?"selected":""}>${inst}</option>`).join("")}</select></div>
            <div><input value="${leg.ticker}" onchange="updateLeg(${i},'ticker',this.value)" style="text-transform:uppercase"></div>
            <div><select onchange="updateLeg(${i},'direction',this.value)">
                <option value="C" ${leg.direction==="C"?"selected":""}>Compra</option>
                <option value="V" ${leg.direction==="V"?"selected":""}>Venda</option></select></div>
            <div><input type="number" value="${leg.quantity}" onchange="updateLeg(${i},'quantity',+this.value)"></div>
            <div><input type="number" value="${leg.taxa}" step="0.005" onchange="updateLeg(${i},'taxa',+this.value)"></div>
            <div><input type="date" value="${document.getElementById('dataNeg').value}" onchange="updateLeg(${i},'data_liq',this.value)"></div>
            <div><select onchange="updateLeg(${i},'corr_type',this.value)">${CORR_TYPES.map(ct =>
                `<option ${ct===leg.corr_type?"selected":""}>${ct}</option>`).join("")}</select></div>
            <div><input type="number" value="${leg.corr_value}" step="0.001" onchange="updateLeg(${i},'corr_value',+this.value)"></div>
            <div>${state.legs.length > 1 ? `<button class="btn-remove" onclick="removeLeg(${i})">✕</button>` : ""}</div>
        </div>`;
    }).join("");
}

function updateLeg(i, field, val) {
    state.legs[i][field] = val;
    processLegs();
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
    try {
        const resp = await fetch("/sim/market-data");
        state.marketData = await resp.json();
        document.getElementById("mktTimestamp").textContent = `Atualizado: ${state.marketData.timestamp}`;
        renderMarketIndicators();
        renderMarketDataTab();
        updateLegsFromMarket();
        processLegs();
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
    const sources = {DI1: m.di1, DOL: m.dol, FRC: m.frc, DAP: m.dap, DDI: m.ddi};
    if (sources[inst]) {
        const c = sources[inst].find(c => c.symb === inst + ticker);
        if (c) return c.last > 0 ? c.last : c.ajuste;
    }
    return null;
}

async function processLegs() {
    const body = {
        legs: state.legs,
        data_neg: document.getElementById("dataNeg").value,
        spot: +document.getElementById("spotInput").value,
    };
    try {
        const resp = await fetch("/sim/process", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
        state.results = await resp.json();
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
    let html = '<div class="av-wrap"><table class="sim-tbl"><tr><th></th><th>Instrumento</th><th class="tc">Ativo</th><th class="tc">Passivo</th><th class="tc">Vcto</th></tr>';
    r.legs.forEach(l => {
        const isBuy = l.direction === "C";
        const dirLabel = isBuy ? "Compra" : "Venda";
        const dirColor = isBuy ? "#3fb950" : "#f85149";
        html += `<tr><td><span style="color:${dirColor};font-weight:600">${dirLabel}</span></td>
            <td class="bold">${l.instrument}</td><td class="tc mono">${l.exp_ativo}</td>
            <td class="tc mono">${l.exp_passivo}</td><td class="tc mono muted">${l.parsed_label}</td></tr>`;
    });
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
    const cols = ["Instr.","Dir.","Lado","Vcto","Liq","DU","DC","Taxa","Final","PU","Financeiro","D.Mac","D.Mod","DV01/un","DV01 Tot","Corr R$","Corr bps"];
    let html = '<table class="sim-tbl"><tr>' + cols.map(c=>`<th>${c}</th>`).join("") + "</tr>";
    r.legs.forEach(l => {
        const isP = l.info_conv === "price";
        html += `<tr>
            <td>${l.instrument}</td><td>${l.direction==="C"?"Compra":"Venda"}</td><td>${l.side}</td>
            <td>${l.parsed_full}</td><td>${l.liq}</td><td>${l.du}</td><td>${l.dc}</td>
            <td class="mono">${isP?l.taxa.toFixed(1):l.taxa.toFixed(4)+"%"}</td>
            <td class="mono">${isP?l.tax_fin.toFixed(1):l.tax_fin.toFixed(4)+"%"}</td>
            <td class="mono">${isP?l.pu.toFixed(1):l.pu.toFixed(2)}</td>
            <td class="mono tr">${isP?"--":"R$ "+l.fin.toLocaleString("pt-BR",{maximumFractionDigits:0})}</td>
            <td class="mono">${l.d_mac.toFixed(2)}</td><td class="mono">${l.d_mod.toFixed(2)}</td>
            <td class="mono">${l.dv01_unit.toFixed(2)}</td><td class="mono">${l.dv01_total.toFixed(0)}</td>
            <td class="mono">${l.corr_brl.toFixed(2)}</td><td class="mono">${l.corr_bps.toFixed(2)}</td></tr>`;
    });
    html += "</table>";
    el.innerHTML = html;
}

function renderSpreadCosts(r) {
    const el = document.getElementById("spreadCosts");
    if (r.strategy.type !== "casada") { el.innerHTML = ""; return; }
    const allin = r.strategy.spread - r.total_corr_bps;
    let html = '<hr class="divider"><div class="two-col"><div><div class="sec-h">Spread All-in</div><table class="sim-tbl"><tr><th>Item</th><th class="tr">Valor</th></tr>';
    html += `<tr><td>Spread bruto</td><td class="tr">${r.strategy.spread.toFixed(2)} bps</td></tr>`;
    r.legs.filter(l=>l.info_conv!=="price").forEach(l => {
        html += `<tr><td>Corretagem ${l.instrument}</td><td class="tr">-${l.corr_bps.toFixed(2)} bps</td></tr>`;
    });
    html += `<tr><td class="bold">Spread all-in</td><td class="tr bold">${allin.toFixed(2)} bps</td></tr></table></div>`;
    html += '<div><div class="sec-h">Custos</div><table class="sim-tbl"><tr><th>Item</th><th class="tr">R$</th><th class="tr">bps</th></tr>';
    r.legs.forEach(l => {
        html += `<tr><td>Corretagem ${l.instrument} (${l.parsed_label})</td><td class="tr">${l.corr_brl.toFixed(2)}</td><td class="tr">-${l.corr_bps.toFixed(2)}</td></tr>`;
    });
    html += `<tr><td class="bold">Total</td><td class="tr bold">R$ ${r.total_corr.toFixed(2)}</td><td class="tr bold">-${r.total_corr_bps.toFixed(2)}</td></tr></table></div></div>`;
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
}

function changeScenario(key) {
    state.scenarioKey = key;
    loadCharts();
}

function renderSliders() {
    const r = state.results; if (!r) return;
    const hasIpca = r.legs.some(l => ["NTN-B","DAP"].includes(l.instrument));
    const hasCupom = r.legs.some(l => ["FRC","DDI"].includes(l.instrument)) || (r.legs.some(l=>l.instrument==="DOL") && r.legs.some(l=>l.instrument==="DI1"));
    const hasFx = r.legs.some(l => l.instrument === "DOL");

    const el = document.getElementById("slidersPanel");
    let html = '<p style="font-size:12px;color:#8b949e;margin-bottom:4px">Choques</p>';
    html += sliderHtml("Pre (bps)", "magnitude", state.magnitude, -50, 50, 1);
    if (hasFx) html += sliderHtml("Câmbio (%)", "deltaFx", state.deltaFx, -10, 10, 0.5);
    if (hasIpca) html += sliderHtml("IPCA (bps)", "deltaIpca", state.deltaIpca, -50, 50, 1);
    if (hasCupom) html += sliderHtml("Cup.Cambial (bps)", "deltaCupom", state.deltaCupom, -50, 50, 1);
    el.innerHTML = html;
}

function sliderHtml(label, key, val, min, max, step) {
    return `<label>${label}</label><input type="range" min="${min}" max="${max}" step="${step}" value="${val}"
        oninput="state.${key}=+this.value;this.nextElementSibling.textContent=this.value;loadCharts()">
        <div class="slider-val">${val}</div>`;
}

async function loadCharts() {
    if (!state.results) return;
    const r = state.results;
    const base = {legs: r.legs, scenario_key: state.scenarioKey, magnitude: state.magnitude,
        delta_fx_pct: state.deltaFx, delta_ipca_bps: state.deltaIpca, delta_cupom_bps: state.deltaCupom};

    const chartReqs = [
        fetch("/sim/charts/curve", {method:"POST", headers:{"Content-Type":"application/json"},
            body:JSON.stringify({...base, di1: state.marketData?.di1||[], dap: state.marketData?.dap||[]})}),
        fetch("/sim/charts/pnl-bars", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(base)}),
        fetch("/sim/charts/pnl-consolidated", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(base)}),
        fetch("/sim/charts/pnl-per-leg", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(base)}),
        fetch("/sim/mtm-table", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(base)}),
    ];

    const [curveR, pnlR, consR, perLegR, mtmR] = await Promise.all(chartReqs);
    const [curve, pnl, cons, perLeg, mtm] = await Promise.all([curveR.json(), pnlR.json(), consR.json(), perLegR.json(), mtmR.json()]);

    const plotCfg = {displayModeBar:false, responsive:true};
    if (curve.data) Plotly.newPlot("chartContainer", curve.data, curve.layout, plotCfg);
    if (pnl.data) Plotly.newPlot("pnlBarsChart", pnl.data, pnl.layout, plotCfg);
    if (cons.data) Plotly.newPlot("pnlConsolidatedChart", cons.data, cons.layout, plotCfg);
    if (perLeg.data) Plotly.newPlot("pnlPerLegChart", perLeg.data, perLeg.layout, plotCfg);

    if (mtm.total_pnl !== undefined) {
        document.getElementById("pnlTotal").innerHTML =
            `<div class="metric"><div class="label">P&L Total do Cenário</div><div class="value ${mtm.total_pnl>=0?"green":"red"}">R$ ${mtm.total_pnl>=0?"+":""}${mtm.total_pnl.toLocaleString("pt-BR",{maximumFractionDigits:0})}</div></div>`;
    }
    if (mtm.table) renderMtmTable(mtm.table, r.legs);

    renderChartTabs();
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
        delta_fx_pct:state.deltaFx, delta_ipca_bps:state.deltaIpca, delta_cupom_bps:state.deltaCupom};
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
    const legLabels = legs.map(l => `${l.instrument} ${l.parsed_label}`);
    let html = '<div class="sim-card"><div class="sim-card-h">Tabela de Cenários MtM (per-leg P&L)</div><div style="overflow-x:auto"><table class="sim-tbl"><tr><th class="tc">Delta (bps)</th>';
    legLabels.forEach(lbl => html += `<th class="tr">${lbl}</th>`);
    html += '<th class="tr bold">Total</th></tr>';
    table.forEach(row => {
        const bg = row.delta === 0 ? ' style="background:#1c2128"' : '';
        html += `<tr${bg}><td class="tc mono">${row.delta>=0?"+":""}${row.delta}</td>`;
        row.pnls.forEach(pnl => {
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
    const m = state.marketData; if (!m) return;
    const el = document.getElementById("mktDataContent");
    let html = `<p class="muted" style="margin-bottom:12px">Atualizado: ${m.timestamp}</p>`;
    html += '<div class="metrics">';
    html += `<div class="metric"><div class="label">CDI Over</div><div class="value">${m.cdi_aa.toFixed(2)}% a.a.</div></div>`;
    html += `<div class="metric"><div class="label">CDI Dia</div><div class="value">${m.cdi_over_dia.toFixed(6)}%</div></div>`;
    html += `<div class="metric"><div class="label">PTAX Venda</div><div class="value">R$ ${m.ptax.toFixed(4)}</div></div>`;
    html += `<div class="metric"><div class="label">Spot USD</div><div class="value">${m.spot_usd>0?"R$ "+m.spot_usd.toFixed(4):"--"}</div></div></div>`;
    html += '<hr class="divider">';
    html += renderMktTable("Curva DI Futuro (B3)", m.di1, ["symb","vcto","last","bid","ask","ajuste"]);
    html += '<div class="two-col">';
    html += renderMktTable("DAP — Cupom IPCA (B3)", m.dap, ["symb","vcto","last","ajuste"]);
    html += renderMktTable("FRC — Cupom Cambial (B3)", m.frc.filter(c=>c.ajuste>0), ["symb","vcto","last","ajuste"]);
    html += '</div><div class="two-col">';
    html += renderMktTable("DOL — Dólar Futuro (B3)", m.dol, ["symb","vcto","last","bid","ask","ajuste"]);
    html += renderMktTable("DDI — Cupom Cambial Sujo (B3)", m.ddi.filter(c=>c.ajuste>0||c.last>0), ["symb","vcto","last","ajuste"]);
    html += '</div>';
    el.innerHTML = html;
}

function renderMktTable(title, data, cols) {
    if (!data || !data.length) return `<div><h3 style="font-size:14px;margin-bottom:8px">${title}</h3><p class="muted">Sem dados</p></div>`;
    let html = `<div><h3 style="font-size:14px;margin-bottom:8px">${title}</h3><div style="overflow-x:auto;max-height:400px"><table class="sim-tbl"><tr>`;
    cols.forEach(c => html += `<th>${c}</th>`);
    html += "</tr>";
    data.forEach(row => {
        html += "<tr>";
        cols.forEach(c => {
            let v = row[c];
            if (typeof v === "number") v = v === 0 ? "—" : (Number.isInteger(v) ? v.toLocaleString("pt-BR") : v);
            html += `<td class="mono">${v}</td>`;
        });
        html += "</tr>";
    });
    html += "</table></div></div>";
    return html;
}

function renderFormulas() {
    document.getElementById("formulasContent").innerHTML = `
    <div class="sim-card"><div class="sim-card-h">Títulos Públicos (TPF)</div><div style="padding:16px">
    <h4>LTN — Zero-Coupon Prefixado</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = 1.000 / (1 + taxa)^(DU/252)</p>
    <p class="muted" style="font-size:11px">Convencao: exponencial, base 252 DU. Truncamento ANBIMA: T-6.</p>
    <h4 style="margin-top:16px">NTN-F — Prefixado com Cupom Semestral</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">Cup_sem = (1,10)^0,5 - 1 = 4,880885%</p>
    <p class="mono" style="font-size:14px">PU = Σ [Cup × VN / (1+TIR)^(DUi/252)] + VN/(1+TIR)^(DUn/252)</p>
    <h4 style="margin-top:16px">NTN-B — IPCA+ com Cupom Semestral</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">Cup_sem = (1,06)^0,5 - 1 = 2,956301%</p>
    <p class="mono" style="font-size:14px">PU = (Cotacao/100) × VNA</p>
    <p class="muted" style="font-size:11px">Cotacao truncada 4 casas. VNA truncado 6 casas.</p>
    <h4 style="margin-top:16px">LFT — Tesouro Selic</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = (Cotacao/100) × VNA_Selic</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Derivativos de Taxa de Juros</div><div style="padding:16px">
    <h4>DI1 — Futuro de DI</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = 100.000 / (1 + taxa)^(DU/252)</p>
    <p class="muted" style="font-size:11px">Face R$ 100.000. Vencimento: 1º DU do mês.</p>
    <h4 style="margin-top:16px">DAP — Futuro de Cupom de IPCA</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = 100.000 / (1 + cupom_IPCA)^(DU/252)</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Derivativos de Câmbio</div><div style="padding:16px">
    <h4>DOL — Dólar Futuro</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">AJ = (PA - PO) × qtd × 50</p>
    <p class="muted" style="font-size:11px">Cotacao em R$ por USD 1.000. Multiplicador: R$ 50/ponto.</p>
    <h4 style="margin-top:16px">DDI — Cupom Cambial Sujo</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = 100.000 / (1 + taxa × DC/360)</p>
    <p class="muted" style="font-size:11px">Convencao: linear, base 360 DC.</p>
    <h4 style="margin-top:16px">FRC — FRA de Cupom Cambial (Limpo)</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">PU = 50.000 / (1 + cupom × DC/360)</p>
    <h4 style="margin-top:16px">Cupom Cambial Implícito (DOL + DI1)</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">cupom = [(Spot×1000/DOL) × (1+DI)^(DU/252) - 1] × 360/DC × 100</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Duration e Risco</div><div style="padding:16px">
    <h4>Duration de Macaulay</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">D_mac = Σ(ti × PVi) / Σ(PVi)</p>
    <h4 style="margin-top:16px">Duration Modificada</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">D_mod = D_mac / (1 + taxa)</p>
    <h4 style="margin-top:16px">DV01</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">DV01 = D_mod × PU × 0,0001</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Interpolação Flat Forward (B3 V14)</div><div style="padding:16px">
    <p class="mono" style="margin:8px 0;font-size:14px">fwd = [(1+r2)^(DU2/252) / (1+r1)^(DU1/252)]^(252/(DU2-DU1)) - 1</p>
    <p class="mono" style="font-size:14px">r_alvo = [(1+r1)^(DU1/252) × (1+fwd)^((DU_alvo-DU1)/252)]^(252/DU_alvo) - 1</p>
    <p class="muted" style="font-size:11px">Premissa: taxa forward constante entre vertices adjacentes.</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Conversões de Taxa</div><div style="padding:16px">
    <h4>CDI + Spread vs Pré</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">(1+CDI) × (1+Spread) = (1+Pré)</p>
    <p class="muted" style="font-size:11px">NUNCA somar CDI + Spread diretamente.</p>
    <h4 style="margin-top:16px">Fisher (Nominal vs Real)</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">(1+nominal) = (1+real) × (1+inflacao)</p>
    <h4 style="margin-top:16px">Linear 360 vs Exponencial 252</h4>
    <p class="mono" style="margin:8px 0;font-size:14px">exp252 = (1 + lin360 × DC/360)^(252/DU) - 1</p>
    </div></div>

    <div class="sim-card"><div class="sim-card-h">Cenários de Curva</div><div style="padding:16px">
    <p class="muted" style="font-size:11px">t = posicao normalizada na curva (-1 = curto, +1 = longo)</p>
    <h4>Paralelo (Shift)</h4><p class="mono" style="font-size:14px">Δi = ± magnitude</p>
    <h4 style="margin-top:12px">Steepener / Flattener</h4><p class="mono" style="font-size:14px">Δi = magnitude × ti</p>
    <h4 style="margin-top:12px">Butterfly</h4><p class="mono" style="font-size:14px">Δi = magnitude × (1 - ti²) - magnitude/2</p>
    </div></div>`;
}

document.addEventListener("DOMContentLoaded", () => { init(); renderFormulas(); });

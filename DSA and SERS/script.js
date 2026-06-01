let temp          =     document.getElementById("temperatura");      // variavel representante da temperatura
let call          =     document.getElementById("comunicacao");      // variavel representante funcionamento da comunicação
let energia       =     document.getElementById("energia");          // variavel representante do nivel de energia
let sessoes       =     [];                                          // lista para armazenar as sessões
let sessaoAtual   =     null;                                        // variavel para armazenar a sessão atual

let tempStatus    =     "";
let callStatus    =     "";
let energiaStatus =     "";

// Função para iniciar a recarga
function iniciarAnalise() {
    
    console.log(temp.value);
    console.log(call.value);
    console.log(energia.value);

    if (temp.value === "" || call.value === "" || energia.value === "") {
        saida.innerHTML =   "Por favor, preencha todos os campos.";
        return;
    } else {
        saida.innerHTML =   "Análise iniciada!<br><br>";
    }

    if (temp.value > 80) {                                          // Verifica se a temperatura é superior a 80 graus
        tempStatus       =   "Alerta de Superaquecimento!!!";
        saida.innerHTML  +=  "Risco de Superaquecimento! Iniciando protocolos de resfriamento.<br>";
    } 
    else {
        tempStatus       =   "Temperatura Normal";
    }
    if (call.checked == true) {                                     // Verifica se a comunicação está funcionando (checkbox marcado)
        callStatus       =   "Comunicação Estável";
    } 
    else {
        callStatus       =   "Falha na Comunicação!!!";
        saida.innerHTML  +=  "Falha na Comunicação! Sistema operando em modo autônomo de tomada de decisão.<br>";
    }
    if (energia.value < 20) {                                       // Verifica se o nível de energia é inferior a 20%
        energiaStatus    =   "Alerta de Baixa Energia!!!";
        saida.innerHTML  +=  "Nível de energia Baixo! Iniciando economia de energia e otimizando o fluxo das baterias solares.<br>";
    }
    else {
        energiaStatus    =   "Nível de Energia Adequado";
    }

    if (tempStatus === "Temperatura Normal" || callStatus === "Comunicação Estável" || energiaStatus === "Nível de Energia Adequado") {
        saida.innerHTML  +=  "Todos os sistemas operando dentro dos parâmetros normais. Monitoramento contínuo em andamento.<br>";
    }

    sessaoAtual = {
        temperatura:    tempStatus,
        energia:        energiaStatus,
        comunicacao:    callStatus,
        data:           new Date().toLocaleString()                 // Registra a data e hora da sessão
    }

    sessoes.push(sessaoAtual);
    sessaoAtual = null;
}

function statusNave() {
    if (sessoes.length === 0) {
        saida.innerHTML = "Nenhuma sessão registrada.";
        return;
    }
    
    if (tempStatus === "Alerta de Superaquecimento!!!" || callStatus === "Falha na Comunicação!!!" || energiaStatus === "Alerta de Baixa Energia!!!") {
        saida.innerHTML = "Status da Nave: ALERTA<br>" +
                            "FALHA DETECTADA!<br><BR>" +
                            tempStatus + "<br>" +
                            callStatus + "<br>" +
                            energiaStatus;
    }
    else {
        saida.innerHTML = "Status da Nave: Normal<br>" +
                            "Sem Falhas Detectadas<br><BR>" +
                            tempStatus + "<br>" +
                            callStatus + "<br>" +
                            energiaStatus;
    }
}

function mostrarHistorico() {
    let saida = document.getElementById("saida");
    
    if (sessoes.length === 0) {
        saida.innerHTML = "<p>Nenhuma sessão registrada.</p>";
        return;
    }

    let tabela =
        "<table class='historico-table'>"   +
        "<thead>"                           +
        "<tr>"                              +
        "<th>Data</th>"                     +
        "<th>Temperatura</th>"              +
        "<th>Energia</th>"                  +
        "<th>Comunicação</th>"              +
        "</tr>"                             +
        "</thead>"                          +
        "<tbody>";


    for (let i = 0; i < sessoes.length; i++) {                      // Itera sobre as sessões registradas para preencher a tabela
        tabela +=                                                   // Adiciona uma linha para cada sessão, exibindo os detalhes de cada uma
            "<tr>" +
            "<td>" + sessoes[i].data            + "</td>" +         // Exibe a temperatura
            "<td>" + sessoes[i].temperatura     + "</td>" +         // Exibe po nível de energia
            "<td>" + sessoes[i].energia         + "</td>" +         // Exibe o horário de início da sessão
            "<td>" + sessoes[i].comunicacao     + "</td>" +         // Exibe o status da comunicação
            "</tr>";
    }

    tabela += "</tbody></table>";
    saida.innerHTML = tabela;                                       // Exibe a tabela de histórico no elemento de saída
}
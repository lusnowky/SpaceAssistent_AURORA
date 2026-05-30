let temp          =     document.getElementById("temperatura");      // variavel representante da temperatura
let call          =     document.getElementById("comunicacao");      // variavel representante funcionamento da comunicação
let energia       =     document.getElementById("energia");          // variavel representante do nivel de energia
let sessoes       =     [];                                          // lista para armazenar as sessões
let sessaoAtual   =     null;                                        // variavel para armazenar a sessão atual

let tempValue = "";
let callValue = "";
let energiaValue = "";

// Função para iniciar a recarga
function iniciarAnalise() {
    
    console.log(temp.value);
    console.log(call.value);
    console.log(energia.value);

    if (temp.value === "" || call.value === "" || energia.value === "") {
        saida.innerHTML =   "Por favor, preencha todos os campos.";
        return;
    } else {
        saida.innerHTML =   "Análise iniciada!<br>";
    }
    if (temp.value > 80) {                                          // Verifica se a temperatura é superior a 80 graus
        tempValue       =   "Alerta de Superaquecimento";
    } 
    else {
        tempValue       =   "Temperatura Normal";
    }
    if (call.checked == true) {                                     // Verifica se a comunicação está funcionando (checkbox marcado)
        callValue       =   "Comunicação Estável";
    } 
    else {
        callValue       =   "Falha na Comunicação";
    }
    if (energia.value < 20) {                                       // Verifica se o nível de energia é inferior a 20%
        energiaValue    =   "Alerta de Baixa Energia";
    }
    else {
        energiaValue    =   "Nível de Energia Adequado";
    }

    sessaoAtual = {
        temperatura:    tempValue,
        energia:        energiaValue,
        comunicacao:    callValue,
        data:           new Date().toLocaleString()                 // Registra a data e hora da sessão
    }

    sessoes.push(sessaoAtual);
    sessaoAtual = null;

    document.getElementById("saida").innerHTML =                    // Exibe os detalhes da sessão atual
        "Os dados inseridos foram analisados e regisitrados!<br>"
}

function statusNave() {
    if (sessoes.length === 0) {
        saida.innerHTML = "Nenhuma sessão registrada.";
        return;
    }
    
    if (tempValue === "Alerta de Superaquecimento" || callValue === "Falha na Comunicação" || energiaValue === "Alerta de Baixa Energia") {
        saida.innerHTML = "Status da Nave: ALERTA<br>";
    }
    else {
        saida.innerHTML = "Status da Nave: Normal<br>" +
                            "Sem Falhas Detectadas<br><BR>" +
                            tempValue + "<br>" +
                            callValue + "<br>" +
                            energiaValue;
    }

    if (energiaValue === "Alerta de Baixa Energia") {
        saida.innerHTML += "Baixa Energia: Iniciando economia de energia e otimizando o fluxo das baterias solares. <br>";
    }

    if (tempValue === "Alerta de Superaquecimento") {
        saida.innerHTML += "Superaquecimento: Ativando sistema de resfriamento e reduzindo a carga dos sistemas não essenciais. <br>";
    }

    if (callValue === "Falha na Comunicação") {
        saida.innerHTML += "Falha na Comunicação: Sistema operando em modo autônomo de tomada de decisão.<br>";
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
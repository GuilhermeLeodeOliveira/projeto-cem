let equipamentoSelect = document.getElementById("selectEquipamento");
let statusSelect = document.getElementById("selectStatus");
let tabela = document.getElementById("tabelaSolicitacoes");

// Adicione ouvintes de evento "change" a todos os selects
equipamentoSelect.addEventListener("change", filtrarTabela);
statusSelect.addEventListener("change", filtrarTabela);

function filtrarTabela() {
    let equipamentoSelecionado = equipamentoSelect.value;
    let statusSelecionado = statusSelect.value;

    // Selecione todas as linhas da tabela
    let linhas = tabela.querySelectorAll("tbody tr");

    linhas.forEach(function(linha) {
        // Selecione as colunas de "Equipamento" e "Status" na linha
        let equipamentoColuna = linha.querySelector("td:nth-child(5)");
        let statusColuna = linha.querySelector("td:nth-child(6)");

        // Verifique se a linha corresponde aos valores selecionados
        if (
            (!equipamentoSelecionado || equipamentoColuna.textContent === equipamentoSelecionado) &&
            (!statusSelecionado || statusColuna.textContent === statusSelecionado)
        ) {
            // Exiba a linha
            linha.style.display = "";
        } else {
            // Oculte a linha
            linha.style.display = "none";
        }
    });
}

let btnSubmit = document.getElementById("btn-submit");

// Adicione um ouvinte de evento ao botão de envio
btnSubmit.addEventListener("click", function() {
    let checkboxesSelecionados = document.querySelectorAll(".solicitacoes input[type='checkbox']:checked");
    let mensagem = "Você selecionou os seguintes usuários:\n";

    checkboxesSelecionados.forEach(function(checkbox) {
        mensagem += "- " + checkbox.value + "\n";
    });

    // Exiba um pop-up de confirmação com os checkboxes selecionados
    if (window.confirm(mensagem)) {
        // Se o usuário confirmar, envie os dados para o servidor
        document.querySelector(".form-equipamento").submit();
    }else{
        event.preventDefault(); // Impede o envio do formulário se o usuário cancelar
    }

});

let gerarCsv = document.getElementById("gerar-csv"); 

// Adicione um ouvinte de evento ao botão de envio
gerarCsv.addEventListener("click", function() {
    let checkboxesSelecionados = document.querySelectorAll(".solicitacoes input[type='checkbox']:checked");
    let mensagem = "Você selecionou os seguintes usuários:\n";

    checkboxesSelecionados.forEach(function(checkbox) {
        mensagem += "- " + checkbox.value + "\n";
    });

    // Exiba um pop-up de confirmação com os checkboxes selecionados
    if (window.confirm(mensagem)) {
        // Se o usuário confirmar, envie os dados para o servidor
        document.querySelector(".form-equipamento").submit();
    }else{
        event.preventDefault(); // Impede o envio do formulário se o usuário cancelar
    }

});

const selectStatus = document.getElementById("selectStatus");
const agendarForm = document.getElementById("agendar-form");

// Função para atualizar a ação do formulário com base no valor selecionado
function atualizarAcaoFormulario() {

    const selectedValue = selectStatus.value;
    let checkboxes = document.querySelectorAll("input[type='checkbox']");
    const btnSubmit = document.getElementById("btn-submit");
    
    if (selectedValue === "pendente") {
        agendarForm.action = '/administracao/solicitacoes/agendar_treinamento/';
        btnSubmit.value = 'Agendar';
        btnSubmit.style.display = 'block'; // Ou outro estilo desejado
        checkboxes.forEach(checkbox => checkbox.checked = false);
    } else if (selectedValue === "em processo") {
        agendarForm.action = '/administracao/solicitacoes/finalizar_treinamento/';
        btnSubmit.value = 'Finalizar';
        btnSubmit.style.display = 'block';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    } else if (selectedValue === "em palestra") {
        agendarForm.action = '/administracao/solicitacoes/finalizar_palestra/';
        btnSubmit.value = 'Finalizar palestra';
        btnSubmit.style.display = 'block';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    }else if (selectedValue === "palestra realizada") {
        agendarForm.action = '/administracao/solicitacoes/agendar_treinamento/';
        btnSubmit.value = 'Agendar Prova';
        btnSubmit.style.display = 'block';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    }else if (selectedValue === "em prova") {
        agendarForm.action = '/administracao/solicitacoes/finalizar_prova/';
        btnSubmit.value = 'Finalizar prova';
        btnSubmit.style.display = 'block';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    }else if (selectedValue === "prova realizada") {
        agendarForm.action = '/administracao/solicitacoes/agendar_treinamento/';
        btnSubmit.value = 'Agendar Treinamento';
        btnSubmit.style.display = 'block';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    }else if (selectedValue === "finalizado") {
        agendarForm.action = '/administracao/solicitacoes/concluir_treinamento/';
        btnSubmit.style.display = 'none';
        checkboxes.forEach(checkbox => checkbox.checked = false);

    }else{
        btnSubmit.style.display = 'none';
    }
}

// Defina a ação inicial com base no valor inicial do selectStatus
atualizarAcaoFormulario();

// Adicione um ouvinte de evento de mudança para o selectStatus
selectStatus.addEventListener("change", atualizarAcaoFormulario);

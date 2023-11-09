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
        mensagem += "- " + checkbox.value + " - " + checkbox.name + "\n";
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

selectStatus.addEventListener("change", () => {
    const selectedValue = selectStatus.value;
    if (selectedValue === "pendente") {
        agendarForm.action = "{% url 'agendar_treinamento' %}";
    } else if (selectedValue === "em_processo") {
        agendarForm.action = "{% url 'finalizar_treinamento' %}";
    } else if (selectedValue === "finalizado") {
        agendarForm.action = "{% url 'concluir_treinamento' %}";
    }
});
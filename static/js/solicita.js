// Selecione os elementos select
let equipamentoSelect = document.getElementById("equipamento");
let divisaoSelect = document.getElementById("divisao");
let apelidoSelect = document.getElementById("apelido");

// Adicione ouvintes de evento "change" a todos os selects
equipamentoSelect.addEventListener("change", filtrarTabela);
divisaoSelect.addEventListener("change", filtrarTabela);
apelidoSelect.addEventListener("change", filtrarTabela);

function filtrarTabela() {
    let equipamentoSelecionado = equipamentoSelect.value;
    let divisaoSelecionada = divisaoSelect.value;
    let apelidoSelecionado = apelidoSelect.value;

    // Selecione todas as linhas da tabela
    let linhas = document.querySelectorAll(".solicitacoes tbody tr");

    linhas.forEach(function(linha) {
        // Selecione as colunas de "Equipamento" na linha
        let equipamentoColuna = linha.querySelector("td:first-child");

        // Verifique se a linha corresponde aos valores selecionados
        if (
            (!equipamentoSelecionado || equipamentoColuna.textContent === equipamentoSelecionado) &&
            (!divisaoSelecionada || linha.querySelector("td:nth-child(2)").textContent === divisaoSelecionada) &&
            (!apelidoSelecionado || linha.querySelector("td:nth-child(3)").textContent === apelidoSelecionado)
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
    let mensagem = "Você selecionou os seguintes equipamentos:\n";

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

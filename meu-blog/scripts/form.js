document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio real do formulário

    // Captura os valores dos campos
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simula o envio dos dados (aqui você poderia fazer uma requisição AJAX, por exemplo)
    console.log('Nome:', name);
    console.log('E-mail:', email);
    console.log('Mensagem:', message);

    // Exibe o alerta de sucesso
    alert('Mensagem enviada com sucesso!!');

    // Limpa o formulário após o envio
    document.getElementById('contactForm').reset();
});






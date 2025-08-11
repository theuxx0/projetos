const express = require('express');
const path = require('path');
const app = express();

const PORT = process.env.PORT || 3000;

// Servir arquivos estáticos da pasta 'public' (onde vai o index.html e style.css)
app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});

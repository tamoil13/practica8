const express = require('express');
const mysql = require('mysql');

const app = express();

// Configurar la conexión a la base de datos MySQL
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',  // La contraseña que usaste para MySQL en XAMPP
    database: 'usuarios'  // El nombre de la base de datos que usaste en el código de Flask
});

db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// Definir una ruta para obtener datos desde la base de datos
app.get('/names', (req, res) => {
    db.query('SELECT * FROM names', (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ error: 'Failed to retrieve data', details: err.message });
            return;
        }
        res.json(results);  // Devolver los resultados en formato JSON
    });
});

app.listen(3000, () => {  // Iniciar el servidor en el puerto 3000
    console.log('Server started on port 3000');
});

import axios from "axios";

const bcrypt = require('bcrypt');
const mysql = require('mysql2')
const con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "bloodbank"
});


export default function handler(req, res) {
    if (req.method === 'POST') {
        const body = req.body;

        const sql = "SELECT * FROM client WHERE EmailAddress = ?";
        con.query(sql, [body.email], (err, result) => {
            // console.log(result);
            if (err) {
                res.status(500).json({
                    error: err
                });
            } else if (result.length === 0) {
                res.status(401).json({
                    message: "User not found"
                })
            } else {
                const salt = result[0]["PasswordSalt"];
                const hash = bcrypt.hashSync(body.password, salt);
                if (hash === result[0]["PasswordHash"]) {
                    res.status(200).json({
                        message: "Login Successful"
                    });
                } else {
                    res.status(401).json({
                        message: "Login Failed"
                    });
                }
            }
            
        });

    } else {
        res.status(405).send('Method not allowed')
    }
}
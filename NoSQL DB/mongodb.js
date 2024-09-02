// Faça os comandos de instalação do node:
// npm install mongodb
// Rode o arquivo posteriormente usando:
// node ./mongodb.js

const { MongoClient } = require("mongodb");
//let json = require('./books.json');

async function main(){
    const uri = "mongodb://localhost:27017";

    const client = new MongoClient(uri);

    try{
        const db = client.db("store");
        const col = db.collection("books");
        //const res = await col.find().toArray();
        //const res = await col.insertMany(json);
        //Todos os registros, ordenados por autor e depois por páginas DESC, pula 5 registros e retorna os próximos 10.
        /*const res = await col
            .find()
            .sort({author: 1, pages: -1})
            .skip(5)
            .limit(10)
            .toArray();
        console.log(res);*/
        //Resultados com autores diferentes de "Vyasa"
        /*const res = await col
            .find({ author: { $ne: "Vyasa"} })
            .limit(1)
            .toArray();*/
        //Resultados com nº de páginas maior que 300
        /*const res = await col
            .find({ pages: { $gt: 300 } })
            .toArray();*/
        //Resultados com nº de paginas maior que 300 e menor que 1000
        const res = await col
            .find({ pages: { $gt: 300, $lt: 1000 } })
            .toArray();
    }
    catch(e){
        console.error(e);
    }
    finally{
        await client.close();
    }
}

main();
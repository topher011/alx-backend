import express from 'express';
import jsonify from 'jsonify';
import { createClient } from 'redis';
import 

const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

function getItemById (id) {
    for (let i = 0; i < listProducts.length; i++) {
	if (id === listProducts[i].id)
	    return listProducts[i];
    }
};

const app = express();
const port = 1245;
const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById (itemId, stock) {
    client.set(`item.${itemId}`, stock);
};

async function getCurrentReservedStockById (itemId) {
    let result = await getAsync(`item.${itemId}`);
    return result;
}

app.get('/list_products', (req, res) => {
    res.send(jsonify(listProducts));
})

app.get('/list_products/:itemId', (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    const error = {status: "Product not found"}

    if (!item) {
	res.json(error)
	return;
    }
    res.send(jsonify(item));
    return;

    //const currentItem = getCurrentReservedStockById(itemId);
})

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    const error = {status: "Product not found"}
    const insufficient = {status: "Not enough stock available", itemId: 1}
    const reserved = {status: "Reservation confirmed", itemId: 1}

    if (!item) {
	res.json(error)
	return;
    } else if (item.stock < 1) {
	res.json(insufficient);
	return;
    } else {
	reserveStockById(itemId, 1);
	res.json(reserved);
	return;
    }

    const currentItem = getCurrentReservedStockById(itemId);
})

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
})

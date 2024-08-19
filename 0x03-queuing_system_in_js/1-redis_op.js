import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
})

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

async function setNewSchool (schoolName, value) {
    await client.set(schoolName, value, redis.print);
}

async function displaySchoolValue (schoolName) {
    const value = await client.get(schoolName, (err, value) => {
	console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

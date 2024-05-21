#!/usr/bin/node
// Number of films with the given character ID
const request = require('request');
let num = 0;

request.get(process.atgv[2], (error, response, body) => {
	if (error) {
		console.log(error);
	} else {
		const content = JSON.parse(body);
		content.results.forEach((film) => {
			film.characters.forEach((character) => {
				if (charcter.includes(18)) {
					num += 1;
				}
			});
		});
		console.log(num);
	}
});

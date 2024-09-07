#!/usr/bin/node

// const request = require('request');

// const args = process.argv;
// const bUrl = 'https://swapi-api.alx-tools.com/api/films/';

// if (args.length > 2) {
//   request(`${bUrl}${args[2]}/`, (err, _, res) => {
//     if (err) {
//       console.log(err);
//     } else {
//       const charURL = JSON.parse(res).characters;
//       charURL.forEach(e => {
//         new Promise((resolve, reject) => {
//           request(e, (err, _, res) => {
//             resolve(JSON.parse(res).name);
//             reject(err);
//           });
//         }).then(data => console.log(data));
//       });
//     }
//   });
// }

const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;

    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

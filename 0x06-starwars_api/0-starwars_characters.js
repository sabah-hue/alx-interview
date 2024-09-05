#!/usr/bin/env node
const request = require('request');

const args = process.argv;
// const b_url = 'http://swapi-api.alx-tools.com/api/';
const bUrl = 'https://swapi-api.hbtn.io/api/';

if (args.length > 2) {
  request(`${bUrl}films/${args[2]}/`, (err, _, res) => {
    if (err) {
      console.log(err);
    } else {
      const charURL = JSON.parse(res).characters;
      charURL.forEach(e => {
        new Promise((resolve, reject) => {
          request(e, (err, _, res) => {
            resolve(JSON.parse(res).name);
            reject(err);
          });
        }).then(data => console.log(data));
      });
    }
  });
}

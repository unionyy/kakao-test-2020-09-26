const https = require('https');
const { x_auth_token } = require('./token.json');
const BASEURL = 'kox947ka1a.execute-api.ap-northeast-2.amazonaws.com'
const BASEPATH = '/prod/users'


function httpsPost(_data, _path, _headers) {
    const data = JSON.stringify(_data);

    const options = {
        hostname: BASEURL,
        port: 443,
        path: BASEPATH + _path,
        method: 'POST',
        headers: _headers,
    };

    return new Promise((resolve, reject) => {
        const req = https.request(options, (res) => {
            console.log(`statusCode: ${res.statusCode}`)
    
            var dd = "";
            res.on('data', (d) => {
                dd += d;
            });

            res.on('close', () => {
                resolve(dd);
            });
        });

        req.on('error', (error) => {
            console.error(error);
            reject();
        });
    
        req.write(data);
        req.end();
    });
}
function httpsPut(_data, _path, _headers) {
    const data = JSON.stringify(_data);

    const options = {
        hostname: BASEURL,
        port: 443,
        path: BASEPATH + _path,
        method: 'PUT',
        headers: _headers,
    };

    return new Promise((resolve, reject) => {
        const req = https.request(options, (res) => {
            console.log(`statusCode: ${res.statusCode}`)
    
            var dd = "";
            res.on('data', (d) => {
                dd += d;
            });

            res.on('close', () => {
                resolve(dd);
            });
        });

        req.on('error', (error) => {
            console.error(error);
            reject();
        });
    
        req.write(data);
        req.end();
    });
}
function httpsGet(_path, _headers) {
    const options = {
        hostname: BASEURL,
        port: 443,
        path: BASEPATH + _path,
        method: 'GET',
        headers: _headers,
    };

    return new Promise((resolve, reject) => {
        const req = https.request(options, (res) => {
            console.log(`statusCode: ${res.statusCode}`)
    
            var dd = "";
            res.on('data', (d) => {
                dd += d;
            });

            res.on('close', () => {
                resolve(dd);
            });
        });

        req.on('error', (error) => {
            console.error(error);
            reject();
        });
    
        req.end();
    });
}

async function startAPI(_pnum) {
    const headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": x_auth_token 
    }
    const ret = await httpsPost({problem: _pnum}, '/start', headers);

    return JSON.parse(ret);
}

async function locationsAPI(auth_key) {
    const headers = {
        "Content-Type": "application/json",
        "Authorization": auth_key
    }
    const ret = await httpsGet('/locations', headers);
    
    return JSON.parse(ret);
}

async function trucksAPI(auth_key) {
    const headers = {
        "Content-Type": "application/json",
        "Authorization": auth_key
    }
    const ret = await httpsGet('/trucks', headers);
    
    return JSON.parse(ret);
}

async function simulateAPI(auth_key, commands) {
    const headers = {
        "Content-Type": "application/json",
        "Authorization": auth_key
    }
    const ret = await httpsPut({commands: commands}, '/simulate', headers);
    
    return JSON.parse(ret);
}

async function scoreAPI(auth_key) {
    const headers = {
        "Content-Type": "application/json",
        "Authorization": auth_key
    }
    const ret = await httpsGet('/score', headers);
    
    return JSON.parse(ret);
}

async function solve() {
    const a = await startAPI(2);
    const b = await locationsAPI(a.auth_key);
    const c = await trucksAPI(a.auth_key);
    //const d = await scoreAPI(a.auth_key);
    const e = await simulateAPI(a.auth_key, [{"truck_id": 0, "command": [2, 5]}]);
    console.log(e);
}

solve();
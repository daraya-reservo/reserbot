var https = require('https');

const options = {
  hostname: 'app.ctrlit.cl',
  path: '/ctrl/dial/registrarweb/eJUVR0SMli?sentido=0&latitud=&longitud=&rut=2',
};

const req = https.get(options, (response) => {
  let data = '';
  response.on('data', (chunk) => {
    data += chunk
    console.log(data);
  });
  response.on('end', () => {
    return data;
  })
});
req.on('error', (error) => {
  console.error(`Problem with request: ${error.message}`);
  return
});

req.end();
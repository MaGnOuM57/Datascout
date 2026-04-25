#!/usr/bin/env node
/**
 * DataScout Pro - Email Sender (Resend API)
 * Usage: node send-email.js <to> <subject> <body_file>
 */

const https = require('https');
const fs = require('fs');

const API_KEY = 're_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh';
const FROM = 'DataScout Pro <noreply@resend.dev>'; // Default Resend domain

async function sendEmail(to, subject, htmlBody) {
  const data = JSON.stringify({
    from: FROM,
    to: [to],
    subject: subject,
    html: htmlBody
  });

  const options = {
    hostname: 'api.resend.com',
    port: 443,
    path: '/emails',
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      'Content-Length': data.length
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let responseBody = '';
      
      res.on('data', (chunk) => {
        responseBody += chunk;
      });
      
      res.on('end', () => {
        if (res.statusCode === 200 || res.statusCode === 201) {
          resolve(JSON.parse(responseBody));
        } else {
          reject(new Error(`HTTP ${res.statusCode}: ${responseBody}`));
        }
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

// CLI usage
if (require.main === module) {
  const [,, to, subject, bodyFile] = process.argv;
  
  if (!to || !subject || !bodyFile) {
    console.error('Usage: node send-email.js <to> <subject> <body_file>');
    process.exit(1);
  }

  const htmlBody = fs.readFileSync(bodyFile, 'utf-8');

  sendEmail(to, subject, htmlBody)
    .then((result) => {
      console.log('✅ Email sent successfully!');
      console.log(JSON.stringify(result, null, 2));
    })
    .catch((error) => {
      console.error('❌ Error sending email:', error.message);
      process.exit(1);
    });
}

module.exports = { sendEmail };

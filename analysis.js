let fs = require('fs')
let spawn = require('child_process').spawn;


const command = __dirname + '/article_analyzer/article_extraction.py'

const files = {
  input: 'input.txt',
  output: 'output.txt',
  snapshot: 'snapshot.txt',
}

function calculateNewSentiments(urls) {
  if (typeof urls === 'string') urls = [urls]

  let child = spawn('python', ['./article_analyzer/article_extraction.py'], { stdio: ['pipe', 'pipe', process.stderr] });

  let childOutput = ''

  // child.on('exit', () => console.log('exit!'))
  
  child.stdin.setEncoding('utf-8');

  child.stdout.on('data', function (_data) {
    try {
        var data = Buffer.from(_data, 'utf-8').toString();
        childOutput += data;
    } catch (error) {
        console.error(error);
    }
  });

  let promise = new Promise((res, rej) => {
    child.stdout.on('exit', function (_) {
      res(childOutput)
    });
    child.stdout.on('end', function (_) {
      res(childOutput)
    });
    child.on('error', function (error) {
      rej(error)
    });
  })

  urls.forEach(url => {
    child.stdin.write(url + '\r\n');
  })
  child.stdin.end()

  return promise

}

calculateNewSentiments('https://www.foxnews.com/politics/pension-funds-in-iran-on-brink-of-collapse-amid-us-maximum-pressure-campaign').then(output => {
  console.log('output:', output)
})

module.exports = {
  calculateNewSentiments
}
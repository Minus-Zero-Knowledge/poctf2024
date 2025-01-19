# Web 100-3 - The Way Out is Through
## Description
The first Web challenge of the contest and I am so excited to reveal this one! In this challenge you'll run through a simulated web-based cybersecurity training course a la the DoD Cyber Exchange Awareness Challenge. There's just one problem... The cybersecurity training is... Vulnerable??! Oh, the irony! Can YOU handle the HACK OF THE CENTURY??? Head here to find out!

[Don't Let Jeff Down!](http://nvstgt.com/TTiOT/index.html)

## Solution
The link directs to an error page, but closer inspection reveals the following JS in the HTML.
```js
let part_1 = [112, 111, 99, 116].map(x => String.fromCharCode(x)).join('');
let part_2 = atob("Znt1d3NwXw==");
let part_3 = "document.cookie";
let part_4 = "XzdydTdoXw==";
let part_5_hex = [0x31, 0x35, 0x5f, 0x30, 0x75, 0x37, 0x5f, 0x37, 0x68, 0x33, 0x72, 0x33, 0x7d];

console.log("The Tooth is Over There.");
document.cookie = "\u0037\u0068\u0033";
```

If we clean up and refactor some variables, we can form the resulting flag string: 
```js
let p1 = part_1;
let p2 = part_2;
let p3 = "\u0037\u0068\u0033";
let p4 = atob(part_4);
let p5 = part_5_hex.map(x => String.fromCharCode(x)).join('');
let result = `${p1}${p2}${p3}${p4}${p5}`;
console.log(result);
```

## Flag
`poctf{uwsp_7h3_7ru7h_15_0u7_7h3r3}`

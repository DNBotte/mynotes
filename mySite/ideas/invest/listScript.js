// list of titles
var titles = ["Combo Funds", "AI", "Fusion Electricity", "Additive Manufacturing", "Asteroid Mining", "Space Transportation", "Desalinization", "Invasive Species", "Lab Grown Agriculture", "3-D Transportation", "Regenerative Medicine", "Cyborg"];

// title appendages get pushed here
var newTitles = [];

// links get pushed here
var dashes = [];

// destination anchors get pushed here
var pound = [];


for (var i =0; i < titles.length; i++) {  

 var pounder =  "# " + titles[i];
 pound.push(pounder);
   dashes.push("#" + titles[i].replace(/\s+/g, '-'));
 newTitles.push("[" + titles[i] + "]" + "(" + dashes[i] + ")" + "\n"); 
}
console.log(newTitles + " " + dashes + pound);

// Can be used to generate list of topics


// [Anchored Intra-Page Links](#anchored-intrapage-links)
// # Anchored Intrapage Links

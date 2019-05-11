//Removes fields from local table that no longer exist in source table

var local = [2, 4, 6, 8];

function syncLocal(local) {
  var source = [1, 2, 3, 4, 5];
  for (var i = 0; i < local.length; i++) {
    for (var j = 0; j < source.length; j++) {
      if (local[i] == source[j]) {
        local.splice(i, 1); 
    }
  }
}
  console.log(local);
}

syncLocal(local);
//Correct result should be: [6, 8]

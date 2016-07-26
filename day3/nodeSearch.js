
/*
	A node is composed of a value and an associative array of children nodes.
*/

function findLongestConsecutiveNumberWrapper(node, current, long){
	//Base case is node.children.length = 0
	if (node.children.length == 0){
		return long;
	}

	//Traverse children nodes
	
	for(var i=0; i < node.children.length; i++){
		if(node.value + 1 === node.children[i].value){
			current++;
			if(current + 1 > long){
				long++;
			}
			long = findLongestConsecutiveNumberWrapper(node.children[i], current, long);
		}
		else {
			long = findLongestConsecutiveNumberWrapper(node.children[i], 1, long);
		}
		
	}

	return long;

}


function longestConsecutiveNumberSequence(node)
{
	return findLongestConsecutiveNumberWrapper(node, 1, 1);
}


var two1three1 = {"value":3, "children":[]};

var two1one = {"value":2, "children":[]};
var two1two = {"value":3, "children":[]};
var two1three = {"value":5, "children":[two1three1]};

var two1 = {"value":4, "children":[two1one, two1two, two1three]};
var two2 = {"value":6, "children":[]};
var two3 = {"value":1, "children":[]};

var first = {"value":3, "children":[two1, two2, two3]};



var long = 1;
var current = 1;

console.log(longestConsecutiveNumberSequence(first));


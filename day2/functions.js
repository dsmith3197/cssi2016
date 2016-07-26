//Day Two

//Functions
function timestwo(num){
	return 2*num;
}

function timessix(num){
	return timestwo(num) + timestwo(num) + timestwo(num);
}
function roll(){
	return Math.floor((Math.random() * 6)) + 1;
}
function checkout(item1, item2, coupon){
    var subtotal = item1 + item2;
    subtotal = subtotal - subtotal*coupon;
    total = Math.round(subtotal * 109.5) /100;
    return total;
};


console.log(timestwo(4));
console.log(timessix(3));
console.log(roll());
console.log(checkout(5,5,.25));

//Strings

var text = "ELEPHANTBEARMOUSECOW";
var result = text.substring(0,12) + text.substring(12, 17).toLowerCase() + text.substring(17);
console.log(result);

function capitalize(word){
	return word.substring(0,1).toUpperCase() + word.substring(1);
}
function endCapitalize(word){
	return word.substring(0,word.length-1) + word.substring(word.length-1).toUpperCase();
}

console.log(capitalize("carrot"));
console.log(endCapitalize("carrot"));

//Conditions

function skeeterRater(score){
	if(score<150)
	{
		return "Pretty bad";
	}
	else if (score<250)
	{
		return "Decent";
	}
	else if (score<350)
	{
		return "Good";
	}
	else if (score<450)
	{
		return "Great";
	}
	else
	{
		return "Inconceivable";
	}
}

console.log(skeeterRater(300));

function fizzBuzz(num){
	if (num%3 == 0 && num%5 == 0)
	{
		return "Fizzbuzz";
	}
	else if(num%3==0){
		return "Fizz";
	}
	else if(num%5==0){
		return "Buzz";
	}
	else{
		return num;
	}
}

console.log(fizzBuzz(9));
console.log(fizzBuzz(10));
console.log(fizzBuzz(15));
console.log(fizzBuzz(8));


function reverseMidCapitalization(word){
	var mid = (word.length - 1)/2;
	if(word.charAt(mid) == word.charAt(mid).toUpperCase())
	{
		return word.substring(0,mid) + word.charAt(mid).toLowerCase() + word.substring(mid+1);
	}
	else
	{
		return word.substring(0,mid) + word.charAt(mid).toUpperCase() + word.substring(mid+1);
	}
}

console.log(reverseMidCapitalization("bar"));
console.log(reverseMidCapitalization("foobar"));
console.log(reverseMidCapitalization("A"));
console.log(reverseMidCapitalization("ALLCAPS"));
console.log(reverseMidCapitalization(""));

//Arrays

function chopAndFlip(words){
	mid = Math.ceil((words.length)/2);
	second = words.splice(mid, words.length-mid);
	output = second.concat(words);
	return output;
}

console.log(chopAndFlip([1, 2, 3, 4, 5, 6]));
console.log(chopAndFlip(["Romeo", "Juliet"]));
console.log(chopAndFlip(["Macbeth"]));
console.log(chopAndFlip(["To", "be", "or"]));


function doubleNumbers(nums){
	for(var i = 0; i < nums.length; i++){
		alert(nums[i]*2);
	}
	return nums;
}

doubleNumbers([1,2,3,4,5]);

function myFavorites(favs){
	for(var i = 0; i < favs.length; i++){
		alert(favs[i] + "? That is my favorite too!");
	}
}


myFavorites(["Stole the Show", "Car Radio"]);


function reverse(nums){
	var reversed = [];
	for(var i = nums.length - 1; i >= 0; i--){
		reversed.push(nums[i]);
	}
	return reversed;
}

console.log(reverse([1,2,3,4,5,6]));

function twine(one, two){
	if(one.length > two.length){
		var end = two.length;
		var long = one;
	}
	else{
		var end = one.length;
		var long = two;
	}
	var result = [];
	var index = 0;
	while (index < end)
	{
		result.push(one[index]);
		result.push(two[index]);
		index++;
	}
	result = result.concat(long.splice(end, long.length-end));
	return result;
}

console.log(twine([1,2,3,4], [1,2]));

//associative arrays

var student = {"gpa" : 4.0, "year" : "freshman", "house" : "Crimson Yard", "concentration" : "Computer Science"};

function associate(keys, values){
	var result = [];
	for(var i = 0; i < keys.length; i++){
		if(i < values.length){
			result[keys[i]] = values[i];
		}
		else{
			result[keys[i]] = null;
		}
	}
	return result;
}

var keys = ["roses", "violets", "sugar"];
var values = ["red", "blue"];
var result = associate(keys, values);
console.log(result.sugar);






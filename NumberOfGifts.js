/* ----------------------- TASK -------------------------------
  Leo's girlfriend asked him to buy a gift list during his next trip, now he wants to know how many of them will he be able to buy.

  Write a function to help Leo out. The first parameter of the function is Leo's budget; 
  the second one is an array containing the price of each gift. You should return an integer representing the maximum amount of gifts Leo can buy.

  EXAMPLE:
    Maximum budget: 20
    Gift List: [13, 2, 4, 6, 1]
    Should return 4.
*/

/* --------------------- APPROACH ----------------------------
  1. Create a function called howManyGifts that takes 2 parameters, the first paramter is the maxBudget, and the second one is the gifts
  2. Declare 2 variables that contain the sum of the gifts (sumOfAllGifts) and the gifts to buy (giftsToBuy). The sumOfAllGifts is a number and the giftsToBuy is an array
  3. Loop throuhg the gifts and calculate the sum of all the gifts
  4. Compare if sumOfAllGifts is less or equal to the maxBuget, if so, push the gifts to the giftsToBuy, otherwise do nothing
  5. Return the length of the giftsToBuy
*/

// --------------------- SOLUTION ------------------------------
function howManyGifts(maxBudget, gifts){
  let sumOfAllGifts = 0
  let giftsToBuy = []
  
  for(let i = 0; i < gifts.length; i++) {
    let gift = gifts[i];
    sumOfAllGifts = gift + gifts[i];
    if (maxBudget >= sumOfAllGifts) {
      giftsToBuy.push(gift);
    }
  }
  return giftsToBuy.length
}

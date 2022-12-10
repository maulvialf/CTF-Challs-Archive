// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract BlackJack {
    string private flag;
    mapping(address => address) private tables;
    mapping(address => bool) private solved;



    function getFlag() public view returns ( string memory ) {
        if (solved[msg.sender] == true){
            return flag;
        }
        return "You haven't won a match yet";
    }

    function getSolved() public view returns ( bool ) {
        return solved[msg.sender];
    } 


    function solve() public   {
        BlackJackTable table = BlackJackTable(tables[msg.sender]);
        if (table.playerBalance() >= 1000 ){
            solved[msg.sender] = true;
        }

    }

    function newTable() public returns (address){
        BlackJackTable table = new BlackJackTable(msg.sender);
        address tableAddress = address(table);
        tables[msg.sender] = tableAddress;
        return tableAddress;
    }
}

contract BlackJackBase {
    enum Suit{  SPADES, CLUBS, HEARTS, DIAMONDS }
    enum Rank { ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING }
    enum Action {HIT, DOUBLE, STAND, LEAVE}
    struct Card {
        Suit suit;
        Rank rank;
    }
    mapping (Rank => uint) points;

    constructor(){
        points[Rank.TWO] = 2;
        points[Rank.THREE] = 3;
        points[Rank.FOUR] = 4;
        points[Rank.FIVE] = 5;
        points[Rank.SIX] = 6;
        points[Rank.SEVEN] = 7;
        points[Rank.EIGHT] = 8;
        points[Rank.NINE] = 9;
        points[Rank.TEN] = 10;
        points[Rank.JACK] = 10;
        points[Rank.QUEEN] = 10;
        points[Rank.KING] = 10;
    }

}

contract BlackJackDeck is BlackJackBase {

    
    Card[] private cards;
    uint private index;


    constructor ()  {
        index = 0;
        Suit[4] memory all_suits =  [Suit.SPADES, Suit.CLUBS, Suit.HEARTS, Suit.DIAMONDS ]; 
        Rank[13] memory all_ranks  = [Rank.ACE, Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING];
        for (uint s=0; s < 4; s++){
            for (uint r=0; r <13; r++){
                cards.push(
                    Card(all_suits[s], all_ranks[r])
                );
            }
        }
        shuffle();
    }

    function drawCard() public returns (Card memory) {

        if (index >= cards.length) {
            shuffle();
            index = 0;
        }
        return cards[index ++];
    }

    function shuffle() private {
        // You dont really need to know this
    }



}

contract BlackJackTable is BlackJackBase {

    address public playerAddress;
    int public playerBalance;
    BlackJackDeck private deck;
    BlackJackGame private game;


    constructor(address _playerAddress) payable {
       playerBalance = 100;
       playerAddress = _playerAddress;
       deck = new BlackJackDeck();
    }
    
    function play() public returns (int) {
        require (msg.sender == playerAddress);
        game = new BlackJackGame(address(this), playerAddress);
        game.play();
        int outcome = ( game.bet_total() * game.outcome() );
        playerBalance = playerBalance + outcome;
        return outcome;
    }

    function drawCard() public returns (Card memory) {
        require (msg.sender == address(game));
        return deck.drawCard();
    }

}

contract BlackJackGame is BlackJackBase {
    int public bet_total = 0;
    int public bet_size = 5;
    int public outcome = -1;
    bool public started = false;
    
    BlackJackTable private table ;
    BlackJackPlayer private player ;
    Card[] private dealerCards;
    Card[] private playerCards;
    

    constructor(address _tableAddress, address _playerAddress) payable {
        table = BlackJackTable(_tableAddress);
        player = BlackJackPlayer(_playerAddress);
        outcome = -1;
    }

    function getPlayerPoints() private view returns (uint) {
        uint points_tot = 0;
        for (uint i=0; i< playerCards.length; i++){
            if (playerCards[i].rank != Rank.ACE) {
                points_tot += points[playerCards[i].rank ];
            }
        }
        for (uint i=0; i< playerCards.length; i++){
            if (playerCards[i].rank == Rank.ACE) {
                if (points_tot + 11 > 21){
                    points_tot += 1;
                } else {
                    points_tot += 11;
                }
            }
        }
        return points_tot;
    }

    function getDealerPoints() private view returns (uint) {
        uint points_tot = 0;
        for (uint i=0; i< dealerCards.length; i++){
            if (dealerCards[i].rank != Rank.ACE) {
                points_tot += points[dealerCards[i].rank ];
            }
        }
        for (uint i=0; i< dealerCards.length; i++){
            if (dealerCards[i].rank == Rank.ACE) {
                if (points_tot + 11 > 21){
                    points_tot += 1;
                } else {
                    points_tot += 11;
                }
            }
        }
        return points_tot;
    }

    function play() public {
        require ( !started );
        started = true;

        addBet();
        dealerCards.push(table.drawCard());
        dealerCards.push(table.drawCard());
        playerCards.push(table.drawCard());
        playerCards.push(table.drawCard());

        while (true){
            Action action = player.getAction();
            if( action == Action.STAND){
                break;
            } else if (action == Action.HIT){
                playerCards.push(table.drawCard());
                if (getPlayerPoints() > 21) {
                    return;
                }
            } else if( action == Action.DOUBLE){
                addBet();
                playerCards.push(table.drawCard());
                if (getPlayerPoints() > 21) {
                    return;
                }
                break;
            } else if(action == Action.LEAVE){
                bet_total = bet_total/2 + 1;
                return;
            }

        }
        uint dealer_points = getDealerPoints();
        uint player_points = getPlayerPoints();
        if (player_points > dealer_points) {
            outcome = 1;
        }
        return ;
    }

    function addBet() public {
        require (table.playerBalance() > bet_size);
        bet_total += bet_size;
    }

    function getPlayerCards() public returns (Card[] memory){
        return playerCards;
    }

    function getDealerCard() public returns (Card memory){
        return dealerCards[1];
    }
}

contract BlackJackPlayer is BlackJackBase {
    address public blackJackAddress;
    address public blackJackTableAddress;

    constructor(address _blackJackAddress){
        blackJackAddress = _blackJackAddress;
        blackJackTableAddress = BlackJack(blackJackAddress).newTable();
    }

    function getAction() public  returns (Action){
        return Action.DOUBLE;
    }

    function play() public returns (int) {
        return BlackJackTable(blackJackTableAddress).play();
    }
    function balance() public view returns (int) {
        return BlackJackTable(blackJackTableAddress).playerBalance();
    }
}


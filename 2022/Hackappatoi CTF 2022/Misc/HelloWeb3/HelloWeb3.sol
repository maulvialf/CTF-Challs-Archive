// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract HelloWeb3 {
    string private riddle;
    string private riddleAnswer;
    string private flag;
    mapping(address => bool) private solved;


    function getFlag() public view returns ( string memory ) {
        if (solved[msg.sender] == true){
            return flag;
        }
        return "You haven't solved the riddle yet";
    }

    function getSolved() public view returns ( bool ) {
        return solved[msg.sender];
    }

    function getRiddle() public view returns ( string memory )  {
        return riddle;
    }

    function solveRiddle(string calldata candidateAnswer) public   {
        if (keccak256( abi.encodePacked(candidateAnswer)) == keccak256( abi.encodePacked(riddleAnswer))){
            solved[msg.sender] = true;
        }
    }
}

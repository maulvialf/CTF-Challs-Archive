// SPDX-License-Identifier = MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract hacklabs is Ownable{
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _CallCounter;

    string public for_flag;
    string public flag;
    mapping (address => string) public greeter;

    constructor(){
        for_flag = "kingkong";
        flag = "REDACTED:)";
    }

    function greeterCount() external view returns(uint256){
        return _CallCounter.current();
    }

    function greeting() external view returns(string memory){
        if(keccak256(bytes(greeter[msg.sender])) != keccak256(bytes(for_flag))){
            string memory output = string(
                abi.encodePacked(
                    "Hello, ",
                    greeter[msg.sender],
                    ". The greeter has changed ",
                    Strings.toString(_CallCounter.current()),
                    " times."
                )
            );
            return output;
        }else if(keccak256(bytes(greeter[msg.sender])) == keccak256(bytes(for_flag))){
            string memory output = string(
                abi.encodePacked(
                    "Hello, Here is your flag",
                    flag,
                    ". The greeter has changed ",
                    Strings.toString(_CallCounter.current()),
                    " times."
                )
            );
            return output;
        }
    }

    function changeGreeter(string memory newGreeter) public{
        bytes memory b = bytes(newGreeter);
        require(b.length > 0, "Invalid newGreeter. Empty String not allowed.");

        greeter[msg.sender] = newGreeter;
        _CallCounter.increment();
    }

    function reset() external onlyOwner{
        _CallCounter.reset();
    }
}
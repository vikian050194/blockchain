// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0 <0.9.0;

// TODO можно ли и как получать значения энама не в int? на 1 звёздочку

/**
 * @title Elections
 * @dev Голосование на выборах
 */
contract Elections {
    enum State { NotStarted, Registration, Delegating, Voting, Finished }

    State public state;

    address public organizer;

    struct Candidate {
        string name;
        uint votes;
        // address account;
    }

    struct Voter {
        // bool didVote;
        uint count;
        address delegate;
    }

    Candidate[] public candidates;

    mapping(address => Voter) public voters;

    constructor() {
        organizer = msg.sender;
    }

    function setNotStarted() public {
        setState(State.NotStarted);
    }

    function setRegistration() public {
        setState(State.Registration);
    }

    function setDelegating() public {
        setState(State.Delegating);
    }

    function setVoting() public {
        setState(State.Voting);
    }

    function setFinished() public {
        setState(State.Finished);
    }

    function setState(State newState) private {
        require(msg.sender == organizer);
        state = newState;
    }

    function registerCandidate(string memory name) public {
        // TODO узнать есть ли исключения хоть в каком-нибудь виде и попробовать использовать, если есть -  на 1 звёздочку
        // require(msg.sender == organizer);
        require(state == State.Registration, "state is not Registration");
        candidates.push(Candidate({name: name, votes: 0}));
        // candidates.push(Candidate({name: name, votes: 0, account: msg.sender}));
    }

    function registerVoter(address account) public {
        // require(msg.sender == organizer);
        require(state == State.Registration, "state is not Registration");
        // voters[account].didVote = false;
        voters[account].count = 1;
        // candidates.push(Candidate({name: name, votes: 0, account: msg.sender}));
    }

    function delegate(address to) public {
        require(state == State.Delegating, "state is not Delegating");
        require(0 != voters[msg.sender].count, "voter has used all available votes");
        voters[msg.sender].count -= 1;
        voters[to].count += 1;
    }

    function vote(uint candidateIndex) public {
        require(state == State.Voting, "state is not Voting");
        require(0 <= candidateIndex && candidateIndex < candidates.length, "candidate index out of range");
        require(0 != voters[msg.sender].count, "voter has used all available votes");
        candidates[candidateIndex].votes += voters[msg.sender].count;
        // voters[msg.sender].didVote = true;
        voters[msg.sender].count = 0;
    }
}
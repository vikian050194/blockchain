# Elections

## Описание

TODO

## Код

```sol
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0 <0.9.0;

/** 
 * @title Elections
 * @dev Голосование на выборах
 */
contract Elections {
    
     // председатель выборной комиисии - владелец контракта
     // определяет состав кандидатов и голосующих
    address private chairman;
    
    // Избиратели(пул кандидатов и избирателей может пересекатся)
    struct Voter {
        bool didVote; // отдан голос или еще нет
        uint vote; // за кого отдан голос
        uint count; // количество голосов у избирателя(с учетом делигированых голосов)
        address delegate; // кому делигирован голос для выбора
    }
    

    // Кандитат на выборах
    struct Candidate {
        string name; // имя кандидата
        uint votes; // количество голосов за кандидата
    }
    
    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    
    // конструктор создаем голосования
    // председателем назначается владелец контракта
    constructor() public {
        chairman = msg.sender;
        voters[chairman].count = 1;
    }

    /** 
    * @title addCandidate - добавить кандидата
    * @dev добавить кандидата может только председатель
    * @param _name - имя кандидата
    */
    function addCandidate(string _name) public {
        // проверка что вызывающий метод является председателем
        require(msg.sender == chairman, "Only the chairman can add a candidate");

        // не удалось проверить уникальность имени кандидата тк в solidity нет нормального сравнения строк

        // добавляем кандидата в массив
        candidates.push(Candidate({
				name: _name,
				votes: 0
			}));
    }
    
    /** 
    * @title addVoter - добавить избирателя
    * @dev добавить избирателя может только председатель
    * @param _voter - адресс избирателя
    */
    function addVoter(address _voter) public {
        require(msg.sender == chairman, "Only chairperson can give right to vote.");
        // проверяем что избиратель еще не голосовал
        require(!voters[_voter].didVote, "The voter already voted.");
        // проверяем что не имеет голоса
        require(voters[_voter].count == 0);
        // выдаем избирателю один голос
        voters[_voter].count = 1;
    }
    
    /** 
    * @title delegateVote - передать голос
    * @dev передает права голоса другому избирателю
    * @param to - адресс избирателя которому отдается голос
    */
    function delegateVote(address to) public {
        // получаем данные о избирателе, вызвавщем функцию
        Voter storage sender = voters[msg.sender];
        // проверем что он еще не отдал голос
        require(!sender.didVote, "You already voted.");
        // проверяем что он не передает голос сам себе
        require(to != msg.sender, "Self-delegation is disallowed.");

        // проверяем что при передаче голосов не произошол цикл
        while (voters[to].delegate != address(0)) {
            to = voters[to].delegate;
            require(to != msg.sender, "Found loop in delegation.");
        }

        // обновляем состояние избирателей
        sender.didVote = true;
        sender.delegate = to;
        Voter storage delegate_ = voters[to];
        if (delegate_.didVote) {
            // если тот кому передаем голос уже проголосовал, добавляем голос нужному кандидату
            candidates[delegate_.vote].votes += sender.count;
        } else {
            // иначе увеличиваем количество голосов у выбраного избирателя
            delegate_.count += sender.count;
        }
    }

    // отдать голос
    function vote(uint number_candidate) public {
        Voter storage sender = voters[msg.sender];
        require(sender.count != 0, "Has no right to vote");
        require(!sender.didVote, "Already voted.");
        sender.didVote = true;
        sender.vote = number_candidate;

        // добавляем все голоса избирателя кандидату
        candidates[number_candidate].votes += sender.count;
    }
    
    // вернуть имя победителя
    function winnerName() public view
            returns (string winnerName_)
    {
        uint winningVoteCount = 0;
        uint winningNubmer = 0;
        for (uint p = 0; p < candidates.length; p++) {
            if (candidates[p].votes > winningVoteCount) {
                winningVoteCount = candidates[p].votes;
                winningNubmer = p;
            }
        }
        winnerName_ = candidates[winningNubmer].name;
    }

}
```

## Сделать

1. TODO
2. TODO
3. TODO

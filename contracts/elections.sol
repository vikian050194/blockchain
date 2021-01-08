pragma solidity >=0.4.22 <0.7.0;

/** 
 * @title Elections
 * @dev Голосование на выборах
 */
contract Elections {
    
     // председамель выборной комиисии - владелец контракта
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
    
    // конструктор создаем голосования, председателем назначается владелец контракта
    constructor() public {
        chairman = msg.sender;
        voters[chairman].count = 1;
    }
    
    // добавить кандидата, может вызвать только председатель
    function addCandidate(string _name) public {
        require(msg.sender == chairman,
            "Only the chairman can add a candidate");
        // не удалось проверить уникальность имени кандидата тк в solidity нет нормального сравнения строк
        candidates.push(Candidate({
				name: _name,
				votes: 0
			}));
    }
    
    // добавить Избирателя, может вызвать только председатель
    function addVoter(address _voter) public {
        require(msg.sender == chairman,
            "Only chairperson can give right to vote.");
        // проверяем что избиратель еще не голосовал
        require(!voters[_voter].didVote,
            "The voter already voted.");
        // проверяем что не имеет голоса
        require(voters[_voter].count == 0);
        // выдаем избирателю один голос
        voters[_voter].count = 1;
    }
    
    // передача голоса другому избирателю
    function DelegateVote(address to) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.didVote, "You already voted.");
        require(to != msg.sender, "Self-delegation is disallowed.");

        while (voters[to].delegate != address(0)) {
            to = voters[to].delegate;

            // We found a loop in the delegation, not allowed.
            require(to != msg.sender, "Found loop in delegation.");
        }
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
    function Vote(uint number_candidate) public {
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
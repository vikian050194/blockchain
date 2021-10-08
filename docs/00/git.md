# Git

0. [Регистрируемся][github-signup-url] на GitHub
1. [Настраиваем][github-ssh-url] доступ по SSH
2. Делаем [форк][github-fork-url] этого [репозетория][github-blockchain-repo-url]
3. Вносим необходимые изменения и пушим в новую ветку своего форка
```bash
git clone git@github.com:<YOUR_LOGIN_HERE>/blockchain.git
git branch my_awesome_feature_branch_name
git add .
git commit -m"Add all required things"
git push
```
4. [Создаём][github-mr-url] MR из форка в основную репу

[github-signup-url]: https://github.com/signup
[github-fork-url]: https://guides.github.com/activities/forking/
[github-ssh-url]: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[github-blockchain-repo-url]: git@github.com:vikian050194/blockchain.git
[github-mr-url]: https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork

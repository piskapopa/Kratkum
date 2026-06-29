<math><msub><mrow><mi>K</mi></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><msub><mrow><mi>a</mi></mrow><mrow><msub><mrow><mi>t</mi></mrow><mrow><msub><mrow><mi>k</mi></mrow><mrow><msub><mrow><mi>u</mi></mrow><mrow><mi>m</mi></mrow></msub></mrow></msub></mrow></msub></mrow></msub></mrow></msub></mrow></msub></math>
**Kratkum** - это аналог латеха и mathml. Он хуже них для большинства людей, но мне он нравится. Логотип **Kratkum** в **Kratkum** записывается как *K r a t k u m _ _ _ _ _ _*. Чтобы пользоваться *Kratkum*, выполните *Kratkum.py*, введите формулу и затем просмотрите *ddd.html*. А чтобы распространить формулу, можно открыть *ddd.html* в бллкноте и скопировать его, тогдп получится текст в mathml. 
# Базовые операторы
Все операторы ставятся после параметров! Выполняются они по по порядку. Каждый опеоатор имеет определённое количество аргументов, если после него нет скобок с количеством аргументов, то он имеет 2 аргумента.
+ ^ - степень. Например, 2 3 ^ даёт <math><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup></math>.
+ \_ - нижний индекс. Например, ψ ψ 0 \_ \_ даёт <math><msub><mrow><mi>ψ</mi></mrow><mrow><msub><mrow><mi>ψ</mi></mrow><mrow><mi>0</mi></mrow></msub></mrow></msub></math>.
+ ? - склеивает 2 формулы, что может помочь избежать ошибки Exception: Exception (которая означает, что в стеке осталось несколько формул). Например, 2 3 ^ 2 3 ^ ? 2 3 ^ ? даёт <math><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup></math>. Как вы видите, пробела нет. Пробел имеет оператор !, например, 2 3 ^ 2 3 ^ ! даёт <math><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup><mspace width="1px"/><msup><mrow><mi>2</mi></mrow><mrow><mi>3</mi></mrow></msup></math>. Пробел равен буквально 1 пикселю, но он всё равно улучшает читаемость.
+ /, -, \*, +, = - собственно, операторы /, -, \*, +, =. Например, 2 2 + 3 2 + / даёт <math><mrow><mrow><mi>2</mi></mrow><mo>+</mo><mrow><mi>2</mi></mrow></mrow><mo>/</mo><mrow><mrow><mi>3</mi></mrow><mo>+</mo><mrow><mi>2</mi></mrow></mrow></math>, а 2 2 \* 4 = даёт <math><mrow><mrow><mi>2</mi></mrow><mo>*</mo><mrow><mi>2</mi></mrow></mrow><mo>=</mo><mrow><mi>4</mi></mrow></math>. Не пытайтесь написать 2 \* 2 = 4, тогда будет недостаточно аргументов и краткум умрёт.
+ sum или же Σ (3) - сумма. Первый аргумент - под знаком суммы, второй - над знаком суммы, третий - выражение суммы. Например, выражение n 0 = 10 x 0 = n x 2 ^ sum sum даёт <math><munderover><mo>Σ</mo><mrow><mrow><mi>n</mi></mrow><mo>=</mo><mrow><mi>0</mi></mrow></mrow><mrow><mi>10</mi><mrow></munderover><munderover><mo>Σ</mo><mrow><mrow><mi>x</mi></mrow><mo>=</mo><mrow><mi>0</mi></mrow></mrow><mrow><mi>10</mi><mrow></munderover><msup><mrow><mi>x</mi></mrow><mrow><mi>2</mi></mrow></msup></math>.
+   brack или же ⏟ - первый аргумент - то, что над знаком, второй - то, что под ним. Например,  |N| 1,2,3,... brack даёт <math><munderover><mo>⏟</mo><mrow><mi>|N|</mi></mrow><mrow><mi>1,2,3,...</mi><mrow></munderover></math>. 
# Продвинутые возможности
+ Вы можете использовать #\<op>, тогда \<op> станет оператором, работающим точно также, как /, -, * и +. Например, #% 2 2 % даст <math><mrow><mi>2</mi></mrow><mo>%</mo><mrow><mi>2</mi></mrow></math>.
+ Алиасы! Алиасы настраиваются через файл aliases.json. Вот его содержимое по умолчанию:
+ {
    "sum": "Σ",
    "phi": "ψ",
    "teta": "θ",
    "yota": "ι",
    "pi": "π",
    "aleph": "א",
    "_0": "0 _",
    "_1": "1 _",
    "_n": "n _",
    "sigma": "σ",
    "fi": "φ",
    "epsilon": "ε",
    "delta": "δ",
    "triangle": "Δ",
    "brack": "⏟",
    "->": "→"
}
- Например, благодаря алиасам вы можете написать aleph \_0, и тогда получится <math><msub><mrow><mi>א</mi></mrow><mrow><mi>0</mi></mrow></msub></math> без ебли с rtlo. То, как изменять алиасы, вы, думаю, уже поняли.
- А если не хочется алиасов, их можно экранировать, например \sum \sum ^ даёт <math><msup><mrow><mi>sum</mi></mrow><mrow><mi>sum</mi></mrow></msup></math>. 
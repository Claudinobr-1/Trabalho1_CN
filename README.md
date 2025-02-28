# **Resolução do trabalho sobre raízes de funções**

Na primeira questão, cujo objetivo era determinar o tempo necessário para que um circuito RC atinja 90 % de sua carga, foram utilizados dois métodos númericos distintos para chegar a uma aproximação, sendo eles: o método da bisseção e o método de Newton

## **Resultados - Questão 1** 💻

| Método da bisseção | Método de Newton |
|--------------------|--------------------|
| 2.3026275634765625 | 2.3025850929935237 |

### Discussão 📚:

#### Método da bisseção - vantagens

- Fácil de implementar e entender, além de não precisar do cálculo de derivadas;
- Se a função f(x)f(x) for contínua no intervalo [a,b] e f(a)⋅f(b)<0f(a)⋅f(b)<0, o método garantidamente converge para uma raiz;
- Funciona bem para funções não suaves ou com descontinuidades, desde que a raiz esteja no intervalo inicial;
- O número de iterações necessárias para atingir uma precisão desejada pode ser estimado antecipadamente, pois o intervalo é reduzido pela metade a cada iteração.

#### Método da bisseção - desvantagens

- A taxa de convergência é linear (p=1p=1), o que significa que o erro é reduzido pela metade a cada iteração. Isso pode ser ineficiente para problemas que exigem alta precisão;
- O método requer um intervalo [a,b][a,b] onde a função muda de sinal. Se o intervalo inicial não for escolhido corretamente, o método pode falhar;
- Se a função for quase constante próximo à raiz, o método pode demorar muitas iterações para convergir;
- Só encontra uma raiz dentro do intervalo inicial. Se houver múltiplas raízes, é necessário dividir o intervalo e aplicar o método várias vezes.

#### Método de Newton - vantagens

- A taxa de convergência é quadrática (p=2p=2) quando próximo da raiz. Isso significa que o número de dígitos corretos praticamente dobra a cada iteração;
- Requer menos iterações que o método da bisseção para atingir uma precisão alta;
- Quando converge, fornece uma aproximação muito precisa da raiz.

#### Método de Newton - desvantagens

- A convergência só é garantida se a estimativa inicial x0x0​ estiver suficientemente próxima da raiz. Caso contrário, o método pode divergir;
- Requer o cálculo da derivada da função f′(x)f′(x), o que pode ser difícil ou custoso em alguns casos;
- Se f′(x)=0f′(x)=0 em algum ponto, o método pode falhar, pois envolve a divisão por f′(x)f′(x);
- Para funções com curvaturas complexas, o método pode oscilar ou convergir para uma raiz indesejada;
- Ao contrário do método da bisseção, a convergência não é garantida para todas as funções contínuas.

## **Resultados - Questão 2** 💻

O problema para a segunda questão consiste em achar uma das raízes da função f(x)=x^5-3x^3+2x^2-5x+1, partindo do valor inicial x0=1, e adontando-se o valor de tolerância e=0,000001. Aplicando o método de Newton obteve-se o seguinte resultado x≃0.2123809336340521.


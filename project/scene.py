from manim import *

class LetterPairs(Scene):
    def construct(self):
        # Lista de letras
        letters = ["A", "B", "C", "D"]

        # Criar todas as combinações possíveis de 2 letras
        pairs = [Text(f"{a}{b}") for a in letters for b in letters if a != b]

        # Definindo as variáveis para o posicionamento
        start_x = -4  # posição inicial x
        start_y = 2   # posição inicial y
        x_step = 2    # passo horizontal
        y_step = -1   # passo vertical
        max_in_row = 4  # máximo de pares em uma linha

        # Posicionar o primeiro par
        pairs[0].move_to(np.array([start_x, start_y, 0]))
        self.play(Write(pairs[0]))

        # Posicionar os pares restantes
        for i, pair in enumerate(pairs[1:], start=1):
            x = start_x + (i % max_in_row) * x_step
            y = start_y + (i // max_in_row) * y_step
            pair.move_to(np.array([x, y, 0]))
            self.play(Write(pair), run_time=0.5)

        self.wait(2)


class LetterPairs2(Scene):
    def construct(self):
        # Lista de letras
        letters = ["A", "B", "C", "D"]

        # Criar todas as combinações possíveis de 2 letras
        pairs = [Text(f"{a}{b}", font_size=48) for a in letters for b in letters if a != b]

        # Posição inicial e final para as animações
        start_pos = ORIGIN
        end_pos = UP * 3 + RIGHT * 4
        scale_factor = 0.5  # Fator de diminuição do tamanho

        # Variáveis para ajustar a posição dos pares subsequentes
        offset_y = 0

        for pair in pairs:
            # Posicionar o par no centro
            pair.move_to(start_pos)
            
            # Animação: mover e diminuir o tamanho
            self.play(
                pair.animate.scale(scale_factor).move_to(end_pos + DOWN * offset_y),
                run_time=2
            )

            # Ajustar o deslocamento vertical para o próximo par
            offset_y += pair.height * scale_factor + 0.1  # Espaçamento adicional

        self.wait(2)

from manim import *

class AumentarFonte(Scene):
    def construct(self):
        # Crie uma equação com fonte maior
        equation = MathTex("e^{i\\pi} + 1 = 0", font_size=48)
        permutation = MathTex("P(n) = n!", font_size=52)
        #arrange =  MathTex("A(n, k) = \frac{n!}{(n-k)!}", font_size=52)      
        #combination = MathTex("C(n, k) = \frac{n!}{k!(n-k)!}", font_size=52) 
        #permrep = MathTex("P(n; n_1, n_2, \ldots) = \frac{n!}{n_1! \cdot n_2! \cdot \ldots}", font_size=52) 
        #combrep = MathTex("C(n; n_1, n_2, \ldots) = \frac{(n + n_1 - 1)!}{n_1! \cdot (n - 1)!}", font_size=56) 

        # Posicione a equação na tela
        equation.move_to(UP*3)
        permutation.next_to(equation,DOWN)
        # Adicione a equação à cena
        self.add(equation)
        self.add(permutation)
        # Execute a animação
        self.wait(2)


class EquationsWithRectangle(Scene):
    def construct(self):
        # Crie um retângulo amarelo transparente
        rect = SurroundingRectangle(color=YELLOW, buff=0.1, fill_opacity=0.2)

        # Posicione o retângulo no centro da tela
        rect.move_to(LEFT)

        # Adicione o retângulo à cena
        self.play(Create(rect), rate_func=smooth)
        self.wait(3)

        # Crie as equações em LaTeX uma a uma
        equation = MathTex("P(n) = n!", font_size=48)
        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=48)
        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=48)

        # Posicione as equações em um VGroup (grupo vertical)
        equations_group = VGroup(equation, arrange, combination)
        equations_group.arrange(DOWN, buff=0.5)  # Alinhe as equações verticalmente
        equations_group.next_to(rect, LEFT)  # Posicione à direita do retângulo

        # Adicione as equações ao grupo e, em seguida, à cena com animações
        self.play(Write(equations_group),run_time=10)
        self.wait(2)


class EquationsWithRectangle(Scene):
    def construct(self):
        # Crie as equações em LaTeX
        equation = MathTex("P(n) = n!", font_size=64)
        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=64)
        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=48)

        # Posicione as equações em um VGroup (grupo vertical)
        equations_group = VGroup(equation, arrange, combination)
        equations_group.arrange(DOWN, buff=0.5)  # Alinhe as equações verticalmente

        # Crie um retângulo amarelo transparente em volta do grupo
        rect = SurroundingRectangle(equations_group, color=YELLOW, buff=0.1, fill_opacity=0.3)

        # Posicione o grupo e o retângulo no centro da tela
        group_and_rect = VGroup(rect, equations_group)
        group_and_rect.move_to(ORIGIN)

        # Adicione o grupo e o retângulo à cena
        self.play(Create(rect), Write(equations_group))
        self.wait(2)


class Abertura(Scene):
    def construct(self):
        # Crie um retângulo transparente com opacidade amarela
        rect = Rectangle(width=6, height=4, color=YELLOW, fill_opacity=0.1)
        rect.move_to(ORIGIN)

        # Animação para fazer o retângulo aparecer lentamente
        self.play(Create(rect), run_time=3)
        self.wait(1)

        # Crie as equações em LaTeX
        equation = MathTex("P(n) = n!", font_size=48)
        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=48)
        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=48)

        # Posicione as equações à esquerda da tela e uma abaixo da outra
        equations_group = VGroup(equation, arrange, combination)
        equations_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        equations_group.to_edge(LEFT)

        # Animação para fazer as equações aparecerem uma abaixo da outra lentamente
        self.play(FadeIn(equations_group[0]), run_time=2)
        self.play(FadeIn(equations_group[1]), run_time=2)
        self.play(FadeIn(equations_group[2]), run_time=2)
        self.wait(2)

class Abertura2(Scene):
    def construct(self):
        # Crie um retângulo transparente com opacidade amarela
        rect = Rectangle(width=6, height=4, color=YELLOW, fill_opacity=0.1)
        rect.to_edge(LEFT, buff=0.5)

        # Animação para fazer o retângulo aparecer lentamente
        self.play(Create(rect), run_time=3)
        self.wait(1)

        # Crie as equações em LaTeX
        equation = MathTex("P(n) = n!", font_size=48)
        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=48)
        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=48)

        # Posicione as equações dentro do retângulo e uma abaixo da outra
        equations_group = VGroup(equation, arrange, combination)
        equations_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        equations_group.next_to(rect, RIGHT, buff=0.5)

        # Animação para fazer as equações aparecerem gradualmente
        for eq in equations_group:
            self.play(FadeIn(eq), run_time=2)
            self.wait(1)

class Abertura3GPT3(Scene):
    def construct(self):
        # Crie um retângulo transparente com opacidade amarela
        rect = Rectangle(width=6, height=4, color=YELLOW, fill_opacity=0.1)
        rect.to_edge(LEFT, buff=0.5)

        # Crie um grupo para as equações
        equations_group = VGroup()

        # Animação para fazer o retângulo aparecer lentamente
        self.play(Create(rect), run_time=3)
        self.wait(1)

        # Crie as equações em LaTeX e adicione ao grupo uma abaixo da outra
        equation = MathTex("P(n) = n!", font_size=48)
        equation.next_to(rect, RIGHT, aligned_edge=UP, buff=0.5)
        self.play(FadeIn(equation), run_time=2)
        equations_group.add(equation)
        self.wait(1)

        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=48)
        arrange.next_to(equation, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(FadeIn(arrange), run_time=2)
        equations_group.add(arrange)
        self.wait(1)

        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=48)
        combination.next_to(arrange, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(FadeIn(combination), run_time=2)
        equations_group.add(combination)
        self.wait(2)

        # Ajuste a posição final do grupo das equações
        equations_group.move_to(rect)

        # Para manter a visibilidade após a animação
        self.add(equations_group)

class Abertura3GPT4(Scene):
    def construct(self):

        top_text = Text("ANÁLISE COMBINATÓRIA", color=WHITE)
        # Position the text at the top of the screen
        top_text.scale(1) 
        top_text.to_edge(UP)
        # Add the text to the scene
        self.add(top_text)

        # Create a yellow transparent rectangle
        rectangle = RoundedRectangle(corner_radius=0.5, height=5, width=6, color=YELLOW, fill_opacity=0.2)
        rectangle.to_edge(LEFT, buff=1)

        # Define the equations
        equation = MathTex("P(n) = n!", font_size=42)
        arrange = MathTex("A(n, k) = \\frac{n!}{(n-k)!}", font_size=42)
        combination = MathTex("C(n, k) = \\frac{n!}{k!(n-k)!}", font_size=42)

        # Position the equations inside the rectangle
        equation.move_to(rectangle.get_center() + UP)
        arrange.next_to(equation, DOWN, buff=0.5)
        combination.next_to(arrange, DOWN, buff=0.5)

        # Create the animation
        # Play the scene
        self.play(Write(top_text))
        self.wait(3)
        self.play(FadeIn(rectangle, run_time=5))
        self.wait(2)
        self.play(Write(equation, run_time=3))
        self.wait(1)
        self.play(Write(arrange, run_time=3))
        self.wait(1)
        self.play(Write(combination, run_time=3))
        self.wait(2)


class TypeText(Scene):
    def construct(self):
        # Crie um objeto de texto
        question = Text("(ACCESS/2022 - CM Rio Acima) João possui seis livros de Matemática. São eles: Geometria I, Álgebra I, Álgebra II, Análise, Matemática Financeira e Números Complexos. O número de maneiras que ele pode empilhar esses livros de modo que os livros de Álgebra fiquem juntos é:", font_size=20)
        
        # Configure a animação para digitar o texto gradualmente
        self.play(Write(question, run_time=8))
        self.wait(2)  # Aguarde alguns segundos após a digitação

        # Adicione as opções de resposta
        options = [
            "a) 240",
            "b) 120",
            "c) 60",
            "d) 20",
        ]

        answer_group = VGroup(*[Text(option) for option in options])
        answer_group.arrange(DOWN, aligned_edge=LEFT)
        answer_group.next_to(question, DOWN, buff=0.5)

        # Adicione a animação para digitar as opções de resposta
        self.play(Write(answer_group, run_time=6))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in [question, answer_group]])  # Desapareça com o texto


class QuestionGPT4(Scene):
    def construct(self):
        title = Title("Análise Combinatória - Arranjo Simples")

        # Adicione o título à cena
        self.play(Create(title))

        question_text = """
                        (ACCESS/2022 - CM Rio Acima) João possui seis livros de Matemática. São eles:
                        Geometria I, Álgebra I, Álgebra II, Análise, Matemática Financeira e Números Complexos. 
                        O número de maneiras que ele pode empilhar esses livros de modo que os livros de Álgebra 
                        fiquem juntos é:

                        a) 240
                        b) 120
                        c) 60
                        d) 20
                        """

        question = Text(question_text, font="Arial", weight=BOLD, line_spacing=1.5, font_size=22)
        #question.scale(0.5)  # Reduz o tamanho do texto para caber na tela
        question.to_edge(UP, buff=0.5)  # Move o texto para a parte superior da tela
        question.next_to(title,DOWN)

        self.play(Write(question, run_time=10))
        self.wait(3)

        svg = SVGMobject("media/livro1.svg")
        svg.move_to(ORIGIN)  # Mova o SVG para a posição desejada

        # Adicione o SVG à cena
        self.play(Create(svg))

        # Continue com a animação da sua cena

        # Ao final, finalize a cena
        self.wait(2)

class AddVect(Scene):
    def construct(self):
        # Importe o arquivo SVG
        livro1 = SVGMobject("media/livro1.svg")
        livro2 = SVGMobject("media/livro2.svg")
        livro3 = SVGMobject("media/livro2.svg")
        livro4 = SVGMobject("media/livro1.svg")
        
        # Ajuste o tamanho e a posição do SVG conforme necessário
        #svg.scale()  # Ajuste o tamanho
        livro1.move_to(LEFT*3)  # Mova o SVG para a posição desejada
        #livro2.next_to(livro1,DOWN)
        livro2.next_to(livro1, UP) 
        livro2.shift(1.6 * DOWN)
        # Adicione o SVG à cena
        self.play(Create(livro1))
        self.wait(1)
        self.play(Create(livro2))
        self.wait(2)

        sinal_diferente = MathTex("\\neq")
        self.play(Create(sinal_diferente))
        self.wait(2)


        livro3.move_to(RIGHT*3)  # Mova o SVG para a posição desejada
        #livro2.next_to(livro1,DOWN)
        livro4.next_to(livro3, UP) 
        livro4.shift(1.6 * DOWN)
        # Adicione o SVG à cena
        self.play(Create(livro3))
        self.wait(1)
        self.play(Create(livro4))
        # Continue com a animação da sua cena
        # Ao final, finalize a cena
        self.wait(2)

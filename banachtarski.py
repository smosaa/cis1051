from manim import *
%%manim -qm -v WARNING BanachAnimation

class BanachAnimation(MovingCameraScene):
    def construct(self):
        
        
        #Create title
        
        title = MarkupText("<u>Banach Tarski Paradox</u>").set_color_by_gradient(YELLOW,GREEN,ORANGE,BLUE,RED,PURPLE)
        title.move_to(UP*3)
        
        
        #intitialize starting circles as well as the ones they are to transform into
        
        circlepoles = Circle(fill_color = YELLOW, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circlepoles2 = Circle(fill_color = YELLOW, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(RIGHT*5+UP*1)
        

        circlestarting = Circle(fill_color = GREEN, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circlestarting2 = Circle(fill_color = GREEN, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(RIGHT*5+DOWN*2)
        
        
        circleup = Circle(fill_color = ORANGE, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circleup2 = Circle(fill_color = ORANGE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(RIGHT*2.5+UP*1)
        
        circledown = Circle(fill_color = BLUE, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circledown2 = Circle(fill_color = BLUE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(RIGHT*2.5+DOWN*2)

        circleright = Circle(fill_color = RED, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circleright2 = Circle(fill_color = RED, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(UP)

        circleleft = Circle(fill_color = PURPLE, fill_opacity = 0.5, stroke_width = 0, radius = 2.0)
        circleleft2 = Circle(fill_color = PURPLE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).shift(DOWN*2)
        
        
        
        #intitialize text objects that correspond to transformed circle/circle color
    
        P = Text("Poles", color = YELLOW).scale(0.5)
        P.move_to(circlepoles2.get_center())
        P.shift(UP*1.25)
        SP = Text("Starting Points", color = GREEN).scale(0.5)
        SP.move_to(circlestarting2.get_center())
        SP.shift(UP*1.25)
        U = Text("Up Points", color = ORANGE).scale(0.5)
        U.move_to(circleup2.get_center())
        U.shift(UP*1.25)
        D = Text("Down Points", color = BLUE).scale(0.5)
        D.move_to(circledown2.get_center())
        D.shift(UP*1.25)
        L = Text("Left Points", color = PURPLE).scale(0.5)
        L.move_to(circleleft2.get_center())
        L.shift(UP*1.25)
        R = Text("Right Points", color = RED).scale(0.5)
        R.move_to(circleright2.get_center())
        R.shift(UP*1.25)
        
        
        
        #first animation:
        # - title is written
        # - circles are joined on the left of origin
        # - circles are transformed and have respective titles written
        
        self.play(Write(title))
        self.play(circlepoles.animate.shift(LEFT*4))
        self.play(circlestarting.animate.shift(LEFT*4))
        self.play(circleup.animate.shift(LEFT*4))
        self.play(circledown.animate.shift(LEFT*4))
        self.play(circleright.animate.shift(LEFT*4))
        self.play(circleleft.animate.shift(LEFT*4))
        self.play(ReplacementTransform(circlepoles,circlepoles2))
        self.play(Write(P))
        self.play(ReplacementTransform(circlestarting,circlestarting2))
        self.play(Write(SP))
        self.play(ReplacementTransform(circleup,circleup2))
        self.play(Write(U))
        self.play(ReplacementTransform(circledown,circledown2))
        self.play(Write(D))
        self.play(ReplacementTransform(circleright,circleright2))
        self.play(Write(R))
        self.play(ReplacementTransform(circleleft,circleleft2))
        self.play(Write(L))
        self.wait(3)
        
        
        #saves camera for future reset, zooms on left point circle
        
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.5).move_to(circleleft2))
        
        
        #left circle is rotated right, new point sequences spawn and are added to the left circle. title is changed accordingly.
        
        
        newup = Circle(fill_color = ORANGE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleleft2.get_center())
        self.play(FadeIn(newup), runtime= 1)
        self.wait(2)
        lu = Text("Left, Up points").scale(0.5).set_color_by_gradient(PURPLE, ORANGE)
        lu.shift(DOWN*.3)
        self.play(FadeOut(L))
        self.play(Write(lu))
        
        newdown = Circle(fill_color = BLUE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleleft2.get_center())
        self.play(FadeIn(newdown), runtime= 1)
        self.wait(2)
        lud = Text("Left, Up, Down points").scale(0.5).set_color_by_gradient(PURPLE, ORANGE,BLUE)
        lud.shift(DOWN*.3)
        self.play(FadeOut(lu))
        self.play(Write(lud))
        
        newstarting = Circle(fill_color = GREEN, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleleft2.get_center())
        self.play(FadeIn(newstarting), runtime = 1)
        self.wait(2)
        luds = Text("Left, Up, Down, and Starting points").scale(0.5).set_color_by_gradient(PURPLE, ORANGE,BLUE,GREEN)
        luds.shift(DOWN*.3)
        self.play(FadeOut(lud))
        self.play(Write(luds))
        self.wait(3)
        
        # zoom out
        
        self.play(Restore(self.camera.frame))
        
        
        #add needed leftover pieces to complete sphere. new sphere created!
        
        circleright2.move_to(circleleft2.get_center())
        circlepoles2.move_to(circleleft2.get_center())
        self.play(Unwrite(R))
        self.play(Unwrite(P))
        self.play(FadeIn(circleright2))
        self.play(FadeIn(circlepoles2))
        
        self.play(FadeOut(luds))
        newwholetitle = Text("New Sphere Made!", color = WHITE).scale(0.5).set_color_by_gradient(PURPLE,ORANGE,BLUE,GREEN,RED,YELLOW)
        newwholetitle.move_to(circleleft2.get_center())
        newwholetitle.shift(UP*2)
        self.play(Write(newwholetitle))
        
        # moving the new sphere
        
        self.play(FadeOut(circleleft2,newup,newdown,newstarting,circleright2,circlepoles2), runtime = 2)
        self.play(Unwrite(newwholetitle))
        
        
        newwhole = VGroup(circleleft2,newup,newdown,newstarting,circleright2,circlepoles2)
        newwhole.to_edge(DL)
        newwhole.shift(RIGHT*2)
        newwholetitle2 = Text("New Sphere!", color = WHITE).scale(0.5).set_color_by_gradient(PURPLE,ORANGE,BLUE,GREEN,RED,YELLOW)
        newwholetitle2.move_to(newwhole.get_center())
        newwholetitle2.shift(UP*1.3)
        self.play(FadeIn(newwhole))
        self.play(Write(newwholetitle2))
        self.wait(3)
        
        #on to the up piece
        
        self.play(self.camera.frame.animate.scale(0.5).move_to(circleup2))
        
        #new sequences spawn once again through rotating the up piece
        
        newleft = Circle(fill_color = PURPLE, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleup2.get_center())
        newright = Circle(fill_color = RED, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleup2.get_center())
        self.play(Unwrite(U))
        self.play(FadeIn(newleft))
        self.play(FadeIn(newright))
        rotuptext = Text("Up, Left, Right points").set_color_by_gradient(ORANGE,PURPLE,RED).scale(0.5)
        rotuptext.move_to(circleup2.get_center())
        rotuptext.shift(UP*1.25)
        self.play(Write(rotuptext))
        
        #move remaining pieces
        
        circlestarting2.move_to(circleup2.get_center())
        circledown2.move_to(circleup2.get_center())
     
        self.play(FadeIn(circlestarting2))
        self.play(FadeOut(SP))
        self.play(FadeIn(circledown2))
        self.play(FadeOut(D))
        self.play(Unwrite(rotuptext))
        nopoletext = Text("Up, Left, Right + leftover Starting & Down").scale(0.5).set_color_by_gradient(ORANGE,PURPLE,RED,GREEN,BLUE)
        nopoletext.move_to(circleup2.get_center())
        nopoletext.shift(UP*1.25)
        self.play(Write(nopoletext))
        self.play(FadeOut(nopoletext))
        almostdonetext = Text("The sphere is almost done!").set_color_by_gradient(ORANGE,PURPLE,RED,GREEN,BLUE).scale(0.5)
        almostdonetext.move_to(circleup2.get_center())
        almostdonetext.shift(UP*1.25)
        self.play(Write(almostdonetext))
        self.play(Restore(self.camera.frame))
        
        self.wait(3)
        
        #fill in poles/starting point
        
        imaginarypoles = Circle(fill_color = YELLOW, fill_opacity = 0.5, stroke_width = 0, radius = 1.0).move_to(circleup2.get_center())
        
        self.play(FadeIn(imaginarypoles))
        
        #move final sphere
        
        self.play(FadeOut(almostdonetext))
        self.play(FadeOut(circleup2,circlestarting2,circledown2,newleft,newright,imaginarypoles))
        secondsphere = VGroup(circleup2,circlestarting2,circledown2,newleft,newright,imaginarypoles)
        secondsphere.to_edge(UL)
        secondsphere.shift(DOWN*2+RIGHT*2)
        sphere2text = Text("The Second Sphere Has Been Created!").set_color_by_gradient(ORANGE,PURPLE,RED,GREEN,BLUE,YELLOW).scale(0.5)
        sphere2text.move_to(secondsphere.get_center())
        sphere2text.shift(UP*1.3)
        self.play(FadeIn(secondsphere))
        self.play(Write(sphere2text))
        self.wait(4)

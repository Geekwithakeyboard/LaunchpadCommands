import sys
import time

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

def main():

    mode = None

    if launchpad.LaunchpadPro().Check( 0 ):
        lp = launchpad.LaunchpadPro()
        if lp.Open( 0 ):
            print("Launchpad Pro")
            mode = "Pro"

    elif launchpad.LaunchpadProMk3().Check( 0 ):
        lp = launchpad.LaunchpadProMk3()
        if lp.Open( 0 ):
            print("Launchpad Pro Mk3")
            mode = "ProMk3"

    elif launchpad.LaunchpadMiniMk3().Check( 1 ):
        lp = launchpad.LaunchpadMiniMk3()
        if lp.Open( 1 ):
            print("Launchpad Mini Mk3")
            mode = "MiniMk3"

    elif launchpad.LaunchpadLPX().Check( 1 ):
        lp = launchpad.LaunchpadLPX()
        if lp.Open( 1 ):
            print("Launchpad X")
            mode = "LPX"
            
    elif launchpad.LaunchpadMk2().Check( 0 ):
        lp = launchpad.LaunchpadMk2()
        if lp.Open( 0 ):
            print("Launchpad Mk2")
            mode = "Mk2"
            yee=5
            x=0
            y=1
            
            while True:
                        print("Colour:")
                        x = input()
                        if x == "end":
                            lp.Reset()
                            lp.Close()
                        else:
                            lp.LedAllOn( int(x) )
                            print("Colour set to " + x )
                        
                        
                

             









if __name__ == '__main__':
    main()



from musicpy import *

written_song = '''
(D6) (A/C#) (Bm7) (A/C#)

(D6) (A/C#) (Bm7) (A/C#)

(D6)Turns out (A/C#) not every dog (Bm7) (A/C#) has his day

(D6) (A/C#) (Bm7) (A/C#)

(D6) So sad, (A/C#) so suddenly (Bm7) (A/C#) gone away

(D6) (A/C#) (Bm7) (A/C#)

(D6) Wish there were more (A/C#) that I (Bm7) could do (A/C#)

(D6) (A/C#) (Bm7) (A/C#)

(D6) Any time you're (A/C#) hearin' this

(C6) Sister, know my (Bm7) heart goes out to you (A)
'''

print(written_song)

d6 = C("D6", pitch=4, duration=1)       
a_csharp = C("A/C#", pitch=3, duration=1)
bm7 = C("Bm7", pitch=3, duration=1)
c6 = C("C6", pitch=3, duration=1)
a = C("A", pitch=3, duration=1)

for _ in range(8):
    play(d6, wait=True)
    play(a_csharp, wait=True)
    play(bm7, wait=True)
    play(a_csharp, wait=True)

play(d6, wait=True)
play(a_csharp, wait=True)
play(c6, wait=True)
play(bm7, wait=True)
play(a, wait=True)

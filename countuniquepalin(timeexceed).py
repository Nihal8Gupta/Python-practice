#count unique palindrome
from itertools import combinations
s="zqpppgacudvmqekmefkzyyfrffeylqrwxlupvskyonqsbclwwgnzbktzelwuhehxrxmqcnepxokialxxwciqsetcsqcsszpeobeiwwedtbisyhexyatammupmfrllpawhqvfebjdappicczehrsooztjatixvtvbmdwikffbozncspuslwgoqypmsmvwghfdmutfpkbjufqrgbhotcikoyvfvxmmadelwxmvybnoroapixubdvijnepeduiwshcwjvhnejafcnuxeimwiiucznzfakwdibwwixcttatqffhnurhecyocoohyuoeixobaxbjcksxqrljiftvcxtocusciqtmydxgjexiwimbcmvhjonkscobhlpggembfslzoisertsvcpiclikprpviqbfdptvtrlhqlfwhurxysxzppnwwbxzaozchalpqsklfedovjkhwdaqdxrzdduwxsyqllvkflamtshyoaamjpzcsnwthnnpgqrrroppxnalxoijzhesphugqporhtamdbugqhgtpxtrjeugenazzpvvtkjrsepvbgvbmmmyxgrkgnlhujinycnjvpqhhugplrgrunrziaabknrjsgaqbpxfpdycpjtquecehrblzurruguhbkzgvebzfkqcolpclgabsuamqaakdikasumksvbfjrudnzihbzqjwivthfozrhkcrmxleaazgkuqmzvzaiiskfrnywntgbtmaxqgqaqxvcpvbvcpqbfivtkdroizfbebhtejegpduqjewcaysphsumddhlgerpspcvhkoezzqwznmqfbcdvxmexbjfgqxlcbneanbglpktxfcfgkfxbpblfpejlfjhiaohcmktfheuyxpof"
count=0
ans=set(combinations(s,3))
ans=list(filter(lambda i:True if i==i[::-1] else False,ans))
print(ans)
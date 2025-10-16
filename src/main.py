from match.dfa import matchStringToDfa
from parsing.dfa import loadDfaFromFile
from parsing.epsilon_removal import removeEpsilonProductions
from parsing.gramatic import stringToGramatic
from utils.argument_parsing import parseLexerArgs
from utils.character_parsing import regexToStandarizeRegex
from utils.file_parsing import fileReader

if __name__ == "__main__":

    parse_arguments = parseLexerArgs();

    lines:list[str] = fileReader(parse_arguments.gramatics_file); 

    # instead of building the dfa from the regex again and again
    dfa = loadDfaFromFile("files/gramatic-dfa.json")

    unparsed_gramatic: list[str] = list()
    
    for line in lines:
        parsed_line = regexToStandarizeRegex(line)

        if matchStringToDfa(dfa, parsed_line) == False:
            print("Not all lines in the grammar, repect the grammar regex")
            exit(1)

        unparsed_gramatic.append(line)

    gramatic = stringToGramatic(unparsed_gramatic)

    removeEpsilonProductions(gramatic)
    # now that we have checked them, we start
 




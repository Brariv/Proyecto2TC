from parsing.epsilon_removal import removeEpsilonProductions
from parsing.gramatic import stringToGramatic
from utils.argument_parsing import parseLexerArgs
from utils.character_parsing import regexToStandarizeRegex
from utils.file_parsing import fileReader
from cyk.cyk_parsing import cyk_parse
from cyk.grammar_parsing import grammar_parsing


if __name__ == "__main__":

    parse_arguments = parseLexerArgs();
    parse_phrase = "she eats a cake with a fork"

    lines:list[str] = fileReader(parse_arguments.gramatics_file); 

    unparsed_gramatic: list[str] = list()
    
    for line in lines:
        parsed_line = regexToStandarizeRegex(line)

        unparsed_gramatic.append(line)

    gramatic = stringToGramatic(unparsed_gramatic)

    CNF = removeEpsilonProductions(gramatic)
    # now that we have checked them, we start
    
    CNF = grammar_parsing(CNF)

    CYK = cyk_parse(parse_arguments.string.split(), CNF)

    print("\n=== CYK ===")
    if (CYK):
        print(f"The phrase '{parse_arguments.string}' is valid according to the grammar.")
    else:
        print(f"The phrase '{parse_arguments.string}' is NOT valid according to the grammar.")


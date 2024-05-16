{-
 - Better operation:
 -	Take flag(s) for lowercase, uppercase, or preserve-case output
 -
 - Advanced operation:
 - 	Take flag for title case, detecting words that should/shouldn't be capitalized in a title
 - 	Numbers -> Words
 - 		Treat each number as one word, or as multiple?
 - -}
import System.Environment
import Data.Char

-- Get first letters
gfl :: (String x) => [x] -> x
gfl [] = []
gfl s = map head s

{-
 - TODO:
 -   Just outputting capitals would be trivial
 -   so next step will be handling CLI arg
 -}

main = do
    input <- getArgs
    putStrLn $ id $ gfl input --equiv to putStrLn(id(gfl input))
    --putStrLn $ map toUpper $ id $ gfl input
    --putStrLn $ map toLower $ id $ gfl input

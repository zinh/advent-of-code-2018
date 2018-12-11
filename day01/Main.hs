module Main where

main :: IO ()
main = do
  content <- readFile "input.txt"
  putStrLn $ (show . calc . lines) content

calc :: [String] -> Int
calc [] = 0
calc (x:xs) = case x of
                ('+':n) -> calc xs + (read n)
                ('-':n) -> calc xs - (read n)
                otherwise -> calc xs

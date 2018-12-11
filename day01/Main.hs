module Main where

import qualified Data.Map as M (Map, lookup, insert, empty)
import Debug.Trace (trace)

main :: IO ()
main = do
  content <- readFile "input.txt"
  putStrLn $ (show . calc . lines) content
  putStrLn $ show $ repeatCalc (cycle (lines content)) M.empty 0

calc :: [String] -> Int
calc [] = 0
calc (x:xs) = calc xs + (convertToInt x)

convertToInt :: String -> Int
convertToInt s = case s of
                   ('+':n) -> (read n)
                   ('-':n) -> (-(read n))

repeatCalc :: [String] -> M.Map Int Bool -> Int -> Int
repeatCalc (x:xs) m currentSum = 
  case M.lookup newSum m of
    Just _ -> newSum
    Nothing -> repeatCalc xs newMap newSum
  where newSum = currentSum + (convertToInt x)
        newMap = M.insert newSum True m

module Lib
    ( someFunc, countChar,
    containNChar
    ) where

import qualified Data.Map as M (Map, empty, insertWith, toList)
import Data.List (foldl')

someFunc :: IO ()
someFunc = putStrLn "someFunc"

checksum :: [String] -> Int
checksum xs = 
  where (char2, char3) = foldl' (\(a, b) s -> s) (0, 0) xs

countChar :: String -> M.Map Char Int
countChar str = countChar' M.empty str

countChar' :: M.Map Char Int -> String -> M.Map Char Int
countChar' m [] = m
countChar' m (c:cs) = countChar' newMap cs
  where f newVal oldVal = newVal + oldVal
        newMap = M.insertWith f c 1 m

containNChar :: Int -> M.Map Char Int -> Bool
containNChar n m = f (M.toList m)
  where f ((_, count):xs) = if count == n then True else f xs
        f _ = False

module Main (main) where

import qualified Data.ByteString.Lazy as B
import Data.Maybe (fromMaybe)
import Decrypt (decrypt)
import Encrypt (encrypt)
import System.Environment (getArgs, getProgName)

encryptFile :: FilePath -> FilePath -> IO ()
encryptFile input output =
	fmap encrypt (B.readFile input) >>=
	writeFile output

decryptFile :: FilePath -> FilePath -> IO ()
decryptFile input output =
	fmap decrypt (readFile input) >>=
	B.writeFile output

act :: [String] -> Maybe (IO ())
act [operation, input, output]
	| operation `elem` ["-e", "--encrypt"] = Just $ encryptFile input output
	| operation `elem` ["-d", "--decrypt"] = Just $ decryptFile input output
act _ = Nothing

main :: IO ()
main = do
	args <- getArgs
	fromMaybe
		(do
			progName <- getProgName
			putStrLn $ "Usage: " ++ progName ++ " <operation> <input> <output>"
			putStrLn "\t-e, --encrypt: converts the input file to the 42 language;"
			putStrLn "\t-d, --decrypt: converts the input file from the 42 language.")

		(act args)

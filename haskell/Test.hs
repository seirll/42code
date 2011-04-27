module Main (main) where

import qualified Data.ByteString.Lazy as B
import Data.Char (ord)
import Decrypt (decrypt)
import Encrypt (encrypt)
import Test.QuickCheck (label, quickCheck)

main :: IO ()
main =
	quickCheck $ label "bijection"
		(\string ->
			let bytes = stringToByteString string in
			(decrypt . encrypt) bytes == bytes)

stringToByteString :: String -> B.ByteString
stringToByteString =
	B.pack .
	map (fromIntegral . ord)

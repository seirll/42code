module Encrypt (encrypt) where

import qualified Data.ByteString.Lazy as B

encrypt :: B.ByteString -> String
encrypt =
	unlines .
	reverse .
	B.foldl'
		(\acc byte -> unwords (replicate (fromIntegral byte) "42") : acc)
		[]

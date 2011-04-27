module Decrypt (decrypt) where

import qualified Data.ByteString.Lazy as B

decrypt :: String -> B.ByteString
decrypt =
	B.pack .
	map (fromIntegral . length . words) .
	lines

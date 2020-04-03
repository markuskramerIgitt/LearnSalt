# Network traffic

## grains.items 

The grains have a size of 4263 Bytes

TX: 2.76KB
RX: 4.78KB
TX: 2.69KB
RX: 4.78KB

## test.version

TX: 2.76KB
RX: 1.99KB

## saltutil.sync_modules

The only module has 1031 bytes

TX: 7.65KB
RX: 5.32KB

TX is + ~5KB than grains.item
RX is ~ grains.item

## Influence of Salt settings...

auth_events: False
minion_data_cache_events: False

## Measurement command

iftop -f "net 192.168.43.59 and not port 22 and not port db-lsp-disc"



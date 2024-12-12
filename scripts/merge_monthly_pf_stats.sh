# Run as CLI 
cd /Users/pedro/extreme_precipitation_in_gpm/data/monthly_pf_stats

csvstack gpm_pf_stats.$REGION.*.csv > merged.gpm_pf_stats.$REGION.csv

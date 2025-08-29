
class SqlUtils:
    """组装Insert、Select、Update、Delete SQL字符串语句"""

    @staticmethod
    def GetKeys(target):
        keys = set()
        if isinstance(target, dict) or isinstance(target, tuple):
            [keys.add(key) for key in target]

        if isinstance(target, list):
            [[keys.add(key) for key in item] for item in target]

        return list(keys)

    @staticmethod
    def InsertSqlStr(tb_name, insert_vals, duplicate_key_update_columns=None):
        tb_fields = None
        tb_values = None

        if isinstance(insert_vals, dict):
            tb_insert_fields = []
            tb_insert_values = []
            for key in insert_vals:
                tb_insert_fields.append(key)
                tb_insert_values.append(repr(insert_vals[key]))
            tb_fields = '(' + ','.join(tb_insert_fields) + ')'
            tb_values = '(' + ','.join(tb_insert_values) + ')'

        if isinstance(insert_vals, list):
            tb_insert_fields = []
            tb_insert_values = []
            for field in insert_vals[0]:
                tb_insert_fields.append(field)

            for val in insert_vals:
                tb_insert_values.append('(' + ','.join(repr(val[field]) for field in tb_insert_fields) + ')')

            tb_fields = '(' + ','.join(tb_insert_fields) + ')'
            tb_values = ','.join(tb_insert_values)

        if tb_fields is None or tb_values is None:
            return None

        tb_insert_sql = 'insert into %s' % tb_name + tb_fields + ' values ' + tb_values

        if isinstance(duplicate_key_update_columns, list) and len(duplicate_key_update_columns) > 0:
            tb_duplicate_key_update_columns = ' on duplicate key update ' + ','.join(
                f'{column}=values({column})' for column in duplicate_key_update_columns)
            return tb_insert_sql + tb_duplicate_key_update_columns

        return tb_insert_sql

    @staticmethod
    def SelectSqlStr(tb_name, select_columns="*", where_vals=None):
        tb_columns = '*'

        # 元祖
        if isinstance(select_columns, tuple):
            tb_columns = repr(select_columns)

        # 数组
        if isinstance(select_columns, list):
            tb_columns = ','.join(select_columns)

        fields = SqlUtils.GetKeys(where_vals)

        # 查询条件：字典
        tb_where = None
        if isinstance(where_vals, dict):
            tb_where_values = [f"{field}='{where_vals[field]}'" for field in fields]
            tb_where = ' and '.join(tb_where_values)

        # 查询条件：列表
        if isinstance(where_vals, list):
            tb_where_values = []
            for val in where_vals:
                tb_where_values.append('(' + ','.join(repr(val[field]) for field in fields) + ')')

            tb_where = '(' + ','.join(fields) + ')' + ' in (' + ','.join(tb_where_values) + ')'

        tb_select_sql = 'select ' + tb_columns + ' from %s' % tb_name
        if tb_where is not None:
            return tb_select_sql + ' where ' + tb_where
        return tb_select_sql

    @staticmethod
    def UpdateSqlStr(tb_name, update_vals=None, where_fields=None):
        if update_vals is None:
            return None

        if where_fields is None:
            return None

        fields = SqlUtils.GetKeys(update_vals)
        tb_where_values = []
        tb_update_set_values = []
        if isinstance(update_vals, dict):
            for field in fields:
                if field in where_fields:
                    tb_where_values.append(f"{field} = {repr(update_vals[field])}")
                else:
                    tb_update_set_values.append(f"{field} = {repr(update_vals[field])}")

        tb_update_sql = 'update ' + tb_name + ' set ' + ' , '.join(tb_update_set_values) + ' where ' + ' and '.join(
            tb_where_values)
        return tb_update_sql

    @staticmethod
    def DeleteSqlStr(tb_name, delete_vals=None, match_mode=None):
        if delete_vals is None:
            return None

        tb_where_fields = SqlUtils.GetKeys(delete_vals)
        tb_delete_sql = "delete from %s" % tb_name
        if isinstance(delete_vals, dict):
            if match_mode is None:
                match_mode = "="
            tb_where_values = " and ".join([f"{key}{match_mode}{repr(delete_vals[key])}" for key in tb_where_fields])
            tb_delete_sql += " where " + tb_where_values

        if isinstance(delete_vals, list):
            if match_mode is None:
                match_mode = "in"
            tb_where_values = ','.join(
                ['(' + ','.join([repr(delete_val[field]) for field in tb_where_fields]) + ')' for delete_val in
                 delete_vals])
            tb_delete_sql += " where " '(' + ','.join(
                tb_where_fields) + ') ' + match_mode + ' (' + tb_where_values + ')'

        return tb_delete_sql